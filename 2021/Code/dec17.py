
def probe_launcher(x,y,N):
    max_height = 0
    all_start_vel = set()
    for vx in range(1,N):
        for vy in range(-N,N):
            all_y = [0]
            this_x = 0
            this_y = 0 
            this_vx = vx
            this_vy = vy
            for t in range(N*2):
                this_x += this_vx
                this_y += this_vy
                this_vx -= 1 if this_vx!=0 else 0
                this_vy -= 1
                all_y.append(this_y)
                if x[0] <= this_x <= x[1] and y[0] <= this_y <= y[1]:
                    this_max_height = max(all_y)
                    max_height = max(max_height, this_max_height)
                    all_start_vel.add((vx,vy))
    return max_height, len(all_start_vel)


if __name__ == '__main__':
    for name, (x, y, N) in zip(["test", "real"], [[[20,30], [-10,-5], 100], [[48,70], [-189,-148], 200]]):
        max_height, nr_starts = probe_launcher(x,y,N)
        print(f'\n{name}:')
        print('max height:', max_height)
        print('nr of start velocities:', nr_starts)
    print()
