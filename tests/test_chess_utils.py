from logic.chess_utils import find_deviation, read_pgn, pgn_string_to_game
from logic.deviation_result import DeviationResult

PGN_PATH = 'pgns/'

def test_find_deviation_white():
    ref_game = read_pgn(PGN_PATH + 'carlsen-nakamura-2020.pgn')
    my_game = read_pgn(PGN_PATH + 'harpseal-rayrey784.pgn')
 
    assert(find_deviation(ref_game, my_game) == DeviationResult(6, 'Qc2', 'Bf4', 'White'))

def test_find_deviation_black():
    ref_game = read_pgn(PGN_PATH + 'ref-acc-dragon-1.pgn')
    my_game = read_pgn(PGN_PATH + 'acc-dragon-test-1.pgn')

    assert(find_deviation(ref_game, my_game) == DeviationResult(11, 'b6', 'a6', 'Black'))

def test_find_deviation_when_equal():
    ref_game = read_pgn(PGN_PATH + 'carlsen-nakamura-2018.pgn')

    assert(find_deviation(ref_game, ref_game) == None)