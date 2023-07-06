import React from 'react';

function User({ user }) {
    return (
        <div>
            <b>{user.username}</b>
            <span>({user.email})</span>
        </div>
    )
}

function UserList() {
    const users = [
        {
            id: 1,
            username: 'developer',
            email: 'public.developer@gmail.com'
        },
        {
            id: 2,
            username: 'tester',
            email: 'public.tester@gmail.com'
        },
        {
            id: 3,
            username: 'moon',
            email: 'public.moon@gmail.com'
        }
    ];

    return (
        <div>
            {users.map(user => (
                <User user={user} key={user.id} />
            ))}
        </div>
    );
}

export default UserList;