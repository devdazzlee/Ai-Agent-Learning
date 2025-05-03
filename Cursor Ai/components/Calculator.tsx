'use client';
import { useState } from 'react';

export default function Calculator() {
    const [display, setDisplay] = useState('0');
    const [equation, setEquation] = useState('');
    const [hasResult, setHasResult] = useState(false);

    const handleNumber = (number: string) => {
        if (hasResult) {
            setDisplay(number);
            setEquation(number);
            setHasResult(false);
        } else {
            setDisplay(display === '0' ? number : display + number);
            setEquation(equation + number);
        }
    };

    const handleOperator = (operator: string) => {
        setHasResult(false);
        setDisplay('0');
        setEquation(equation + operator);
    };

    const handleEqual = () => {
        try {
            const result = eval(equation);
            setDisplay(result.toString());
            setEquation(result.toString());
            setHasResult(true);
        } catch (error) {
            setDisplay('Error');
            setEquation('');
        }
    };

    const handleClear = () => {
        setDisplay('0');
        setEquation('');
        setHasResult(false);
    };

    return (
        <div className="bg-gray-800 p-6 rounded-xl shadow-2xl w-80">
            <div className="bg-gray-700 p-4 rounded-lg mb-4">
                <div className="text-gray-400 text-sm h-6">{equation}</div>
                <div className="text-white text-3xl font-bold text-right">{display}</div>
            </div>
            <div className="grid grid-cols-4 gap-2">
                <button onClick={handleClear} className="col-span-2 bg-red-500 text-white p-4 rounded-lg hover:bg-red-600">
                    AC
                </button>
                <button onClick={() => handleOperator('/')} className="bg-gray-600 text-white p-4 rounded-lg hover:bg-gray-700">
                    ÷
                </button>
                <button onClick={() => handleOperator('*')} className="bg-gray-600 text-white p-4 rounded-lg hover:bg-gray-700">
                    ×
                </button>
                {[7, 8, 9, 4, 5, 6, 1, 2, 3].map((num) => (
                    <button
                        key={num}
                        onClick={() => handleNumber(num.toString())}
                        className="bg-gray-500 text-white p-4 rounded-lg hover:bg-gray-600"
                    >
                        {num}
                    </button>
                ))}
                <button onClick={() => handleOperator('-')} className="bg-gray-600 text-white p-4 rounded-lg hover:bg-gray-700">
                    -
                </button>
                <button onClick={() => handleOperator('+')} className="bg-gray-600 text-white p-4 rounded-lg hover:bg-gray-700">
                    +
                </button>
                <button onClick={() => handleNumber('0')} className="col-span-2 bg-gray-500 text-white p-4 rounded-lg hover:bg-gray-600">
                    0
                </button>
                <button onClick={handleEqual} className="bg-blue-500 text-white p-4 rounded-lg hover:bg-blue-600">
                    =
                </button>
            </div>
        </div>
    );
} 