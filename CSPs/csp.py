class csp:
    variables={}
    constraints={}
    domain={}
    def __init__(self,variables,domain,constraints):
        self.variables=variables
        self.domain=domain
        self.constraints=constraints
    
    def selectUnassignedVariable(self,assignment):
        for item in self.variables:
            if item not in assignment:
                return item

    def orderDomainValues(self, var,assignment):
        return self.domain
    
    def constraintsChecking(self,assignment,checkedConstraints=[]):
        newConstraints=[]
        for params in self.constraints:
            if params in checkedConstraints:
                continue
            constraint_function=self.constraints[params]
            keys = params.split(",")
            keys_available = True
            arr=[]
            for key in keys:
                keys_available= key in assignment
                if not keys_available: break
                arr.append(assignment[key])
            if not keys_available: continue
            if not constraint_function(arr): return False,[]
            newConstraints.append(params)
        return True,newConstraints
    
    def goalReached(self,assignment):
        return len(assignment) == len(self.variables)
    
    def backtrackingSearch(self,assignment={},checkedConstraints=[]):
        # if assignment is complete, return assignment

        if self.goalReached(assignment):
            return assignment
        # Select unassigned variable
        var = self.selectUnassignedVariable(assignment)
        # For Each value that can be given to variable

        for value in self.orderDomainValues(var,assignment):
            # Add Value to Assignment
            assignment[var]=value
            # if Constraints are satisfied, Forward the assignment
            ConstraintsChecked,newConstraints =self.constraintsChecking(
                assignment,checkedConstraints
            )
            if ConstraintsChecked:
                result = self.backtrackingSearch(
                    assignment,checkedConstraints+newConstraints
                )
                # if it reached the goal, return the result
                if self.goalReached(result):
                    return result
            # Remove value from assignment
            del assignment[var]

        if len(assignment) == 0:
            print("==Failed to Find Answer==")
        return assignment