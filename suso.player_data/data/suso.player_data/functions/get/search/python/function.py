import math

for i1 in range(2):
    s1 = i1 * 16 + 1
    e1 = i1 * 16 + 16
    m1 = math.floor((s1+e1)/2)
    with open("{}_{}.mcfunction".format(s1,e1), "w") as f:
        f.write("execute if score @s suso.pldata.id matches ..{} run function suso.player_data:get/search/{}_{}\n".format(m1,s1,m1))
        f.write("execute if score @s suso.pldata.id matches {}.. run function suso.player_data:get/search/{}_{}\n".format(m1+1,m1+1,e1))
    for i2 in range(2):
        s2 = s1 + i2 * 8
        e2 = s1 + i2 * 8 + 7
        m2 = math.floor((s2+e2)/2)
        with open("{}_{}.mcfunction".format(s2,e2), "w") as f:
            f.write("execute if score @s suso.pldata.id matches ..{} run function suso.player_data:get/search/{}_{}\n".format(m2,s2,m2))
            f.write("execute if score @s suso.pldata.id matches {}.. run function suso.player_data:get/search/{}_{}\n".format(m2+1,m2+1,e2))
        for i3 in range(2):
            s3 = s2 + i3 * 4
            e3 = s2 + i3 * 4 + 3
            m3 = math.floor((s3+e3)/2)
            with open("{}_{}.mcfunction".format(s3,e3), "w") as f:
                f.write("execute if score @s suso.pldata.id matches ..{} run function suso.player_data:get/search/{}_{}\n".format(m3,s3,m3))
                f.write("execute if score @s suso.pldata.id matches {}.. run function suso.player_data:get/search/{}_{}\n".format(m3+1,m3+1,e3))
            for i4 in range(2):
                s4 = s3 + i4 * 2
                e4 = s3 + i4 * 2 + 1
                m4 = math.floor((s4+e4)/2)
                print(i1, i2, i3, i4, "start:", s4, "end:", e4, "mid:", m4)
                with open("{}_{}.mcfunction".format(s4,e4), "w") as f:
                    f.write("execute if score @s suso.pldata.id matches {} run data modify storage suso.pldata working_data set from storage suso.pldata {}\n".format(s4,s4))
                    f.write("execute if score @s suso.pldata.id matches {} run data modify storage suso.pldata working_data set from storage suso.pldata {}\n".format(e4,e4))