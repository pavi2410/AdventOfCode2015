fun main() {
    fun part1(input: String): Int {
        return input.map { if (it == '(') 1 else -1 }.sum()
    }

    fun part2(input: String): Int {
        var s = 0
        var p = 0
        input.map { if (it == '(') 1 else -1 }.dropWhile {
            s += it
            p++
            s != -1
        }
        return p
    }

    val testInput: Map<String, Int> = mapOf(
        "(())" to 0,
        "()()" to 0,
        "(((" to 3,
        "(()(()(" to 3,
        "))(((((" to 3,
        "())" to -1,
        "))(" to -1,
        ")))" to -3,
        ")())())" to -3
    )

    for ((key, value) in testInput) {
        check(part1(key) == value)
    }

    val input = readInput("Day01")[0]
    println(part1(input))
    println(part2(input))
}
