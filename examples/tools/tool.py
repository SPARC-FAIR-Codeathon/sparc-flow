from sparc_me import Dataset_Api

import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    api_tools = Dataset_Api()

    dataset = api_tools.get_dataset_latest_version_pensieve(262)

    # api_tools.download_dataset(dataset["id"])

    sel = 14  # select form parameter tables above which train to plot
    param = (0, sel)
    real_ch_names = ['Cuff 1', 'Cuff 2', 'Cuff 3', 'LIFE 1', 'LIFE 2', 'LIFE 3', 'Micro 1', 'Micro 2',
                     'Micro 3']  # for vagus

    time = [0.000000000000000000e+00,
            8.191999999999999629e-04,
            1.638399999999999926e-03,
            2.457599999999999889e-03,
            3.276799999999999852e-03,
            4.095999999999999815e-03,
            4.915199999999999778e-03,
            5.734399999999999741e-03,
            6.553599999999999703e-03,
            7.372799999999999666e-03,
            8.191999999999999629e-03,
            9.011200000000000460e-03,
            9.830399999999999555e-03,
            1.064960000000000039e-02,
            1.146879999999999948e-02,
            1.228800000000000031e-02,
            1.310719999999999941e-02,
            1.392640000000000024e-02,
            1.474559999999999933e-02,
            1.556480000000000016e-02,
            1.638399999999999926e-02,
            1.720319999999999835e-02,
            1.802240000000000092e-02,
            1.884160000000000001e-02,
            1.966079999999999911e-02,
            2.048000000000000168e-02,
            2.129920000000000077e-02,
            2.211839999999999987e-02,
            2.293759999999999896e-02,
            2.375680000000000153e-02,
            2.457600000000000062e-02,
            2.539519999999999972e-02,
            2.621439999999999881e-02,
            2.703360000000000138e-02,
            2.785280000000000047e-02,
            2.867199999999999957e-02,
            2.949119999999999867e-02,
            3.031040000000000123e-02,
            3.112960000000000033e-02,
            3.194879999999999942e-02,
            3.276799999999999852e-02,
            3.358719999999999761e-02,
            3.440639999999999671e-02,
            3.522560000000000274e-02,
            3.604480000000000184e-02,
            3.686400000000000093e-02,
            3.768320000000000003e-02,
            3.850239999999999913e-02,
            3.932159999999999822e-02]
    voltages = [[-1.194679728397433872e-05,
                 -1.980733829726684289e-05,
                 -1.077133905927803561e-03,
                 -1.519773320369282514e-04,
                 4.358444211166163332e-05,
                 1.658965415525065864e-05,
                 2.398549602516097313e-06,
                 -1.332335275220263179e-06,
                 1.629816851936227506e-06,
                 4.550925948376061261e-07,
                 -2.440652094473894876e-07,
                 -1.256780047896774447e-07,
                 -1.604059700341167774e-07,
                 -1.366082574509440694e-07,
                 6.310354307689493841e-08,
                 1.457346526672138439e-08,
                 -1.628435072394222375e-07,
                 -6.812635356888434155e-09,
                 5.664900883157117720e-08,
                 -5.565218230427167767e-09,
                 2.460946088137883220e-07,
                 5.694319531931366159e-08,
                 -2.056334398814257176e-08,
                 1.748808934360601829e-07,
                 1.773989087065118717e-07,
                 -1.101112467177508824e-07,
                 -1.075328597482854415e-07,
                 3.386144369441476939e-08,
                 1.897932070755456980e-08,
                 -2.771581229295496183e-08,
                 -4.256350579346231629e-08,
                 2.369912349741317857e-07,
                 1.700902709291848032e-07,
                 -1.165152584466342702e-08,
                 2.526520739717943143e-08,
                 7.121820226943954045e-08,
                 7.056591199310062196e-09,
                 -5.769651171224500800e-08,
                 5.493674015745062083e-08,
                 -1.013383430345409753e-07,
                 9.970229271565001302e-08,
                 -3.204593418913237084e-07,
                 -4.325400556337169854e-07,
                 -6.636738552043014031e-07,
                 -9.158674234832865898e-07,
                 -1.763365287119160062e-06,
                 -2.739152133168838517e-06,
                 -4.476083953312462761e-06,
                 -7.542537164392824152e-06],
                [-1.194679728397433872e-05,
                 -1.980733829726684289e-05,
                 -1.077133905927803561e-03,
                 -1.519773320369282514e-04,
                 4.358444211166163332e-05,
                 1.658965415525065864e-05,
                 2.398549602516097313e-06,
                 -1.332335275220263179e-06,
                 1.629816851936227506e-06,
                 4.550925948376061261e-07,
                 -2.440652094473894876e-07,
                 -1.256780047896774447e-07,
                 -1.604059700341167774e-07,
                 -1.366082574509440694e-07,
                 6.310354307689493841e-08,
                 1.457346526672138439e-08,
                 -1.628435072394222375e-07,
                 -6.812635356888434155e-09,
                 5.664900883157117720e-08,
                 -5.565218230427167767e-09,
                 2.460946088137883220e-07,
                 5.694319531931366159e-08,
                 -2.056334398814257176e-08,
                 1.748808934360601829e-07,
                 1.773989087065118717e-07,
                 -1.101112467177508824e-07,
                 -1.075328597482854415e-07,
                 3.386144369441476939e-08,
                 1.897932070755456980e-08,
                 -2.771581229295496183e-08,
                 -4.256350579346231629e-08,
                 2.369912349741317857e-07,
                 1.700902709291848032e-07,
                 -1.165152584466342702e-08,
                 2.526520739717943143e-08,
                 7.121820226943954045e-08,
                 7.056591199310062196e-09,
                 -5.769651171224500800e-08,
                 5.493674015745062083e-08,
                 -1.013383430345409753e-07,
                 9.970229271565001302e-08,
                 -3.204593418913237084e-07,
                 -4.325400556337169854e-07,
                 -6.636738552043014031e-07,
                 -9.158674234832865898e-07,
                 -1.763365287119160062e-06,
                 -2.739152133168838517e-06,
                 -4.476083953312462761e-06,
                 -7.542537164392824152e-06]
        ,
                [-1.462083138277712432e-06,
                 -2.622262173064377229e-06,
                 -7.534344594908582143e-04,
                 4.759606952424768331e-05,
                 9.223688791069610846e-06,
                 1.677105825408498600e-05,
                 2.933277337991895692e-06,
                 8.110282750876216604e-07,
                 -1.425914101175619564e-06,
                 -1.663120625907863012e-06,
                 -9.908095184916553125e-08,
                 2.624454673115753441e-07,
                 -1.624587473395667151e-07,
                 3.338108641988796370e-08,
                 4.483677957255745166e-08,
                 -2.272849655834033843e-08,
                 6.738530411162273816e-08,
                 -1.318730119721173922e-07,
                 2.174619084598256286e-08,
                 -2.635504384574270156e-08,
                 -2.126007975966536514e-07,
                 -1.018217795072811392e-07,
                 -1.916260472310982058e-08,
                 -6.106306355050666979e-08,
                 -9.495394166931023019e-09,
                 -3.854787158901162777e-09,
                 -1.056476775362339673e-07,
                 4.154432204662217048e-08,
                 5.605603793178550658e-08,
                 -7.432304252075775190e-08,
                 -8.398636677852381007e-08,
                 -1.854658209056216439e-07,
                 -8.286421105874349958e-08,
                 -1.424359400919484305e-07,
                 -2.010722883843532184e-07,
                 7.429247114041876855e-08,
                 6.948458981206337186e-08,
                 -1.446947117729709508e-07,
                 -5.107443403085964430e-08,
                 4.225381293752249147e-10,
                 6.443742709884127751e-08,
                 4.906226138658068876e-08,
                 -9.440736302779392982e-08,
                 -2.710204727223795743e-07,
                 1.652564732815241083e-09,
                 -8.563504499159779379e-08,
                 -4.766724708442070395e-07,
                 -7.328525557563466932e-07,
                 -8.203079358028723468e-07]
                ]

    time = np.array(time)
    voltages = np.array(voltages)

    fig, ax = plt.subplots(figsize=(15, 5))
    for i in range(len(voltages)):  # add desired channels to plot here
        plt.plot(time * 1e3, voltages[i] * 1e6, label=str(real_ch_names[i]))

    plt.xlabel('Time (ms)')
    plt.ylabel('Voltage (\u03BCV)')
    plt.xlim([1, 9])  # 1-9 for Abeta, 1-19 for B
    plt.ylim([-150, 150])  # 150 for Abeta, 20 for B
    plt.legend(loc='upper right', fontsize=18)
    plt.xlabel('Time (ms)', fontsize=20)
    plt.ylabel('Voltage (uV)', fontsize=20)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.show()

    # np.savetxt('output.txt', time)  
    
