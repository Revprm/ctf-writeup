# PGN Encryption [293 Pts]

**Category:** Misc, Stego

**Solves:** -

## Description
> Flag on chess moves here

## Solution

Decode the chess moves using this code [Chess Encryption](https://github.com/WintrCat/chessencryption)

Add these 2 lines at the top

```py
pgn_string = "f3 f6 2. g3 h5 3. g4 Rh6 4. gxh5 g6 5. f4 b6 6. Kf2 Rh8 7. Nf3 Rh6 8. Ke3 Na6 9. Kd4 Rb8 10. Ne5 Rh8 11. Kc3 Rxh5 12. Bh3 Rf5 13. Kc4 d6 14. Nc3 Rxe5 15. Bg4 Re3 16. Bf5 Re6 17. e4 Bb7 18. d3 Rc8 19. Be3 Qd7 20. Nb5 Kf7 21. Qh5+ Ba8 22. Qh7+ Bg7 23. Nxc7 Re8 24. Rhg1 Kf8 25. Bc5 Rc8 26. Bxb6 Bb7 27. Ba5 Qb5+ 28. Kd4 Qe8 29. Rg3 Nh6 30. Nb5"
output_file_path = "output.txt"
```

Call `decode(pgn_string, output_file_path)`

### Flag

`flag{Faustino_Oro_Our_Carlsen}`