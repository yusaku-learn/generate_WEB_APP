window.onload = function() {
    const speechBubble = document.getElementById('speechBubble');
    const inputForm = document.getElementById('inputForm');
    const submitButton = document.getElementById('submitButton');

    const text1 = "これはあなたの心を癒してくれる唯一無二の相棒です。";
    const text2 = "今日の気持ちを教えてください。";

    let index = 0;
    const speed = 100;  // 文字が表示される間隔 (ミリ秒)

    function showText(text, callback) {
        if (index < text.length) {
            speechBubble.innerText += text.charAt(index);  // 1文字ずつ追加
            index++;
            setTimeout(() => showText(text, callback), speed);  // 次の文字を一定時間後に表示
        } else {
            if (callback) {
                setTimeout(callback, 1000);  // 次のテキストを1秒後に開始
            }
        }
    }

    function showSecondText() {
        index = 0;
        speechBubble.innerText = '';  // 1つ目のテキストを消して2つ目を表示
        showText(text2, showInputForm);
    }

    function showInputForm() {
        inputForm.style.display = 'block';  // フォームを表示
        inputForm.style.opacity = 0;
        setTimeout(() => {
            inputForm.style.transition = 'opacity 1s';  // フェードイン効果
            inputForm.style.opacity = 1;
        }, 500);  // 0.5秒後にフォームをフェードイン
    }

    // 最初のテキストを表示し、次のテキストを順番に表示
    showText(text1, showSecondText);
};




