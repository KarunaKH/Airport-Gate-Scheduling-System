import copy

landing=[0]*2000
gates=[0]*2000
takeoff=[0]*2000

class Airport_Scheduling:
    def __init__(self,l,g,t):
        self.l=l
        self.g=g
        self.t=t


    def __read_data(self):
        self.planes = {}
        f = open('input.txt', 'r')
        temp = f.readline().split(" ")
        self.L, self.G, self.T = int(temp[0]), int(temp[1]), int(temp[2])
        self.N = int(f.readline())
        for i in xrange(1, self.N + 1):
            self.planes[i] = {}
            temp = f.readline().split(" ")
            r,m,s,o,c=int(temp[0]), int(temp[1]), int(temp[2]), int(temp[3]), int(temp[4])
            self.planes[i]['R'], self.planes[i]['M'], self.planes[i]['S'], self.planes[i]['O'], self.planes[i]['C']=r,m,s,o,c
        self.initialize_data()


    def initialize_data(self):
        self.unassigned={}
        for i in xrange(1, self.N + 1):
            self.unassigned[i]=-1

        self.assignment={}
        for i in xrange(1, self.N + 1):
            self.assignment[i] = {}
            self.assignment[i]['landing'] = -1
            self.assignment[i]['gate']=-1
            self.assignment[i]['takeoff'] = -1

        self.domain={}
        for i in xrange(1, self.N+1):
            self.domain[i]={}
            self.domain[i]['landing']=list(xrange(0,self.planes[i]['R']+1))
            self.domain[i]['takeoff']=list(xrange(0+self.planes[i]['M']+self.planes[i]['S'],self.planes[i]['R']+self.planes[i]['M']+self.planes[i]['C']+1))


    def valid(self,land_time,gate_time,takeoff_time,takeoff_over):
        if self.l>self.L or self.g>self.G or self.t>self.T:
            return False
        for i in xrange(land_time, gate_time):
            if landing[i]>self.L:
                return False
        for i in xrange(gate_time,takeoff_time):
            if gates[i]>self.G:
                return False
        for i in xrange(takeoff_time,takeoff_over):
            if takeoff[i]>self.T:
                return False
        return True


    def mrv(self):
        domain_lens={}
        for i in xrange(1,self.N+1):
            if self.unassigned[i]==-1:
                list=self.domain[i]['landing']
                domain_lens[i]=len(list)
        list=sorted(domain_lens, key=lambda x:domain_lens[x])
        return list


    def lcv(self,plane):
        conflicts = []
        list=self.domain[plane]['landing']
        for vd in list:
            c=landing[vd]
            if c>0:
                conflicts.append([vd, c-1])
            else: conflicts.append([vd, c])
        list = sorted(conflicts, key=lambda x: x[1])
        lcv_list = []
        for alist in list:
            lcv_list.append(alist[0])
        return lcv_list


    def update(self,plane,land_time,gate_time):
        for i in xrange(land_time,gate_time):
            if landing[i]>=self.L:
                for p in self.domain:
                    list = self.domain[p]['landing']
                    if i in list:
                        list.remove(i)
                    self.domain[p]['landing']=list


    def assign(self,plane,land_time,gate_time,takeoff_time,takeoff_over):
        for i in xrange(land_time, gate_time):
            landing[i]+=1
        for i in xrange(gate_time, takeoff_time):
            gates[i]+=1
        for i in xrange(takeoff_time, takeoff_over):
            takeoff[i]+=1


    def unassign(self,plane,land_time,gate_time,takeoff_time,takeoff_over):
        self.unassigned[plane] = -1
        self.l -= 1
        self.g -= 1
        self.t -= 1
        for i in xrange(land_time, gate_time):
            landing[i]-=1
        for i in xrange(gate_time, takeoff_time):
            gates[i]-=1
        for i in xrange(takeoff_time, takeoff_over):
            takeoff[i]-=1


    def solved(self):
        for p in self.planes:
            if self.unassigned[p]==-1:
                return False
        return True


    def backtrack(self):
        if self.solved():
            return True

        min_value_planes=self.mrv()
        for plane in min_value_planes:
            m=self.planes[plane]['M']
            s=self.planes[plane]['S']
            c=self.planes[plane]['C']
            o=self.planes[plane]['O']
            if self.unassigned[plane]==-1:
                prev_assignment = copy.deepcopy(self.assignment)
                prev_domain = copy.deepcopy(self.domain)

                lcv_list=self.lcv(plane)
                if len(lcv_list)==0: return False

                for land_start in lcv_list:
                    start=land_start+m+s
                    end=land_start+m+c

                    for takeoff_start in xrange(start,end+1):
                        self.assignment[plane]['landing'] =land_start
                        self.assignment[plane]['gate']=land_start+m
                        self.assignment[plane]['takeoff']=takeoff_start

                        self.assign(plane,land_start,land_start+m,takeoff_start,takeoff_start+o)
                        check=self.valid(land_start,land_start+m,takeoff_start,takeoff_start+o)

                        if check:
                            self.l += 1
                            self.g += 1
                            self.t += 1
                            self.unassigned[plane] = 1
                            self.update(plane, land_start, land_start + m)
                            self.backtrack()
                            return True
                        else:
                            self.unassign(plane,land_start,land_start+m,takeoff_start,takeoff_start+o)
                            self.assignment = copy.deepcopy(prev_assignment)
                            self.domain = copy.deepcopy(prev_domain)
        return False

    def main(self):
        airport_schedule=Airport_Scheduling(0,0,0)
        airport_schedule.__read_data()
        result=airport_schedule.backtrack()
        if result:
            n=airport_schedule.N
            result=airport_schedule.assignment
            f=open('output.txt','w')
            for n in xrange(1, n + 1):
                f.write("%s %s\n" % (result[n]['landing'], result[n]['takeoff']))

if __name__=='__main__':
    Airport_Scheduling(0,0,0).main()