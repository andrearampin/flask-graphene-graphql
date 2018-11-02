import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType
from database import db_session, User as UserModel
from sqlalchemy import and_


class Users(SQLAlchemyObjectType):
    class Meta:
        model = UserModel
        interfaces = (relay.Node, )


class createUser(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        email = graphene.String()
        username = graphene.String()

    ok = graphene.Boolean()
    user = graphene.Field(Users)

    def mutate(self, info, name, email, username):
        user = UserModel(name=name, email=email, username=username)
        db_session.add(user)
        db_session.commit()
        ok = True
        return createUser(user=user, ok=ok)


class changeUsername(graphene.Mutation):
    class Arguments:
        username = graphene.String()
        email = graphene.String()

    ok = graphene.Boolean()
    user = graphene.Field(Users)

    def mutate(self, info, email, username):
        query = Users.get_query(info)
        user = query.filter(UserModel.email == email).first()
        user.username = username
        db_session.commit()
        ok = True
        return changeUsername(user=user, ok=ok)


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    user = SQLAlchemyConnectionField(Users)
    all_users = SQLAlchemyConnectionField(Users)
    find_user = graphene.Field(Users, username=graphene.String())

    def resolve_find_user(self, info, username):
        query = Users.get_query(info)
        return query.filter(UserModel.username == username).first()


class FlipMutations(graphene.ObjectType):
    create_user = createUser.Field()
    change_username = changeUsername.Field()


schema = graphene.Schema(query=Query,
                         mutation=FlipMutations,
                         types=[Users])
