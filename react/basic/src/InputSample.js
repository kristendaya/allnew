import React, { useState } from 'react';

function InputSample() {
    const [inputs, setInputs] = useState({
        name: '',
        nickname: ''
    })

    const { name, nickname } = inputs;

    const onChange = (e) => {
        const { value, name } = e.target;
        setInputs({
            ...inputs, //기존 input 객체 복사
            [name]: value
        });
    }

    const onReset = () => {
        setInputs({
            name: '',
            nickname: ''
        })
    }

    return (
        <div>
            <input name="name" onChange={onChange} value={name} placeholder='이름' />
            <input name="nickname" onChange={onChange} value={nickname} placeholder='닉네임' />
            <button onClick={onReset}>초기화</button>
            <div>
                <b>값 : </b>
                {name} ({nickname})
            </div>
        </div>
    );
}

export default InputSample;
