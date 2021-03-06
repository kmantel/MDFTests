import psyneulink as pnl

comp = pnl.Composition(name='comp')
A = pnl.TransferMechanism(name='A')
B = pnl.TransferMechanism(name='B')
C = pnl.TransferMechanism(name='C')
D = pnl.TransferMechanism(name='D')

comp.add_linear_processing_pathway([A, B, C])
comp.add_linear_processing_pathway([A, B, D])

comp.scheduler.add_condition_set({
    A: pnl.AtNCalls(A, 0),
    B: pnl.Always(),
    C: pnl.EveryNCalls(B, 5),
    D: pnl.EveryNCalls(B, 10),
})

comp.run(inputs={A: 1})

# A, B, B, B, B, B, C, A, B, B, B, B, B, {C, D}
print(comp.scheduler.execution_list[comp.default_execution_id])

with open(__file__.replace('.py', '.json'), 'w') as f:
    f.write(comp.json_summary)

comp.show_graph()
