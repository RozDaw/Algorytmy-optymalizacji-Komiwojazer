import matplotlib.pyplot as plt

def plot_solution(route, coords, title="Trasa komiwojażera", position=(100, 100), animate=True):
    delay = 1.0 / (len(route) + 1)

    x_all = [coords[i][0] for i in route + [route[0]]]
    y_all = [coords[i][1] for i in route + [route[0]]]

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_title(title)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.grid(True)
    
    # Ustawienie pozycji okna
    try:
        mng = plt.get_current_fig_manager()
        mng.window.wm_geometry(f"+{position[0]}+{position[1]}")
    except Exception as e:
        print(f"Nie udało się ustawić pozycji okna: {e}")

    # Rysowanie wszystkich punktów z numerami
    for idx, (xi, yi) in enumerate(coords):
        ax.plot(xi, yi, 'bo')
        ax.text(xi, yi, str(idx), fontsize=12, color='red')

    # Linia, która będzie aktualizowana
    line, = ax.plot([], [], 'b-', linewidth=2)

    if animate:
        # Animowane rysowanie trasy
        x_data, y_data = [], []
        for i in range(len(x_all)):
            x_data.append(x_all[i])
            y_data.append(y_all[i])
            line.set_data(x_data, y_data)
            plt.pause(delay)
    else:
        # Statyczny wykres
        line.set_data(x_all, y_all)

    plt.show(block=False)
    plt.pause(0.1)








# import matplotlib.pyplot as plt

# def plot_solution(route, coords, title="Trasa komiwojażera", position=(100,100)):
#     x = [coords[i][0] for i in route + [route[0]]]
#     y = [coords[i][1] for i in route + [route[0]]]

#     fig = plt.figure(figsize=(8, 6))
#     plt.plot(x, y, 'bo-')
#     for idx, (xi, yi) in enumerate(coords):
#         plt.text(xi, yi, str(idx), fontsize=12, color='red')
#     plt.title(title)
#     plt.xlabel("X")
#     plt.ylabel("Y")
#     plt.grid(True)

#     try:
#         mng = plt.get_current_fig_manager()
#         mng.window.wm_geometry("+{}+{}".format(position[0], position[1]))
#     except Exception as e:
#         print(f"Nie udało się ustawić pozycji okna: {e}")


#     plt.show(block=False)
#     plt.pause(0.1)  # pozwala matplotlibowi narysować wykres

