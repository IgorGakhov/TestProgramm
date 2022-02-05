





document.getElementById("start-check").onclick = async (e) => {
    let numA = document.getElementById("a-input-value").value
    let numB = document.getElementById("b-input-value").value

    document.getElementById("result-nod-inp").value = await eel.gcd_middle(numA, numB)()

    document.getElementById("result-a-inp").value = await eel.factorization_middle(numA)()
    document.getElementById("result-b-inp").value = await eel.factorization_middle(numB)()

    e.preventDefault()
    return false
}