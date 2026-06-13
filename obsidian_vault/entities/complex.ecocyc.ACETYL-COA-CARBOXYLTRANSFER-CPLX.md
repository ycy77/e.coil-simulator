---
entity_id: "complex.ecocyc.ACETYL-COA-CARBOXYLTRANSFER-CPLX"
entity_type: "complex"
name: "acetyl-CoA carboxyltransferase"
source_database: "EcoCyc"
source_id: "ACETYL-COA-CARBOXYLTRANSFER-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "ACC"
---

# acetyl-CoA carboxyltransferase

`complex.ecocyc.ACETYL-COA-CARBOXYLTRANSFER-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ACETYL-COA-CARBOXYLTRANSFER-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0ABD5|protein.P0ABD5]], [[protein.P0A9Q5|protein.P0A9Q5]]

## Enriched Summary

Acetyl-CoA carboxyltransferase (ACC) is part of the acetyl-CoA carboxylase complex, catalyzing the second half-reaction, the carboxylation of acetyl-CoA to form malonyl-CoA. Acetyl-CoA carboxylase is inhibited by acylated derivatives of ACP. The inhibition is of a mixed type, i.e. a combination of competitive and noncompetitive inhibition. The competitive nature of the inhibition suggests an interaction with the acetyl-CoA binding site. This in turn suggests that the acyl-ACP is binding with the acetyl-CoA carboxyltransferase component of the enzyme complex . Exogenous long-chain fatty acids causes an increase in acyl-CoA, which causes accumulation of acyl-ACP substrates that inhibit ACC . Potent inhibitors with antibacterial activity have been identified . A crystal structure of the enzyme has been solved at 3.2 Å resolution. The β subunit contains a Zn2+-binding domain, suggesting the ability to bind to DNA . It was then shown that the enzyme is indeed able to bind DNA nonspecifically, and that DNA binding inhibits enzymatic activity . The Zn2+-binding domain of AccD is required both for catalytic activity and for binding to mRNA; the enzyme has higher specificity to mRNA and binds to the coding regions of accA and accD mRNA, inhibiting their translation...

## Biological Role

Catalyzes RXN0-5055 (reaction.ecocyc.RXN0-5055). Component of acetyl-CoA carboxylase complex (complex.ecocyc.ACETYL-COA-CARBOXYLMULTI-CPLX).

## Annotation

Acetyl-CoA carboxyltransferase (ACC) is part of the acetyl-CoA carboxylase complex, catalyzing the second half-reaction, the carboxylation of acetyl-CoA to form malonyl-CoA. Acetyl-CoA carboxylase is inhibited by acylated derivatives of ACP. The inhibition is of a mixed type, i.e. a combination of competitive and noncompetitive inhibition. The competitive nature of the inhibition suggests an interaction with the acetyl-CoA binding site. This in turn suggests that the acyl-ACP is binding with the acetyl-CoA carboxyltransferase component of the enzyme complex . Exogenous long-chain fatty acids causes an increase in acyl-CoA, which causes accumulation of acyl-ACP substrates that inhibit ACC . Potent inhibitors with antibacterial activity have been identified . A crystal structure of the enzyme has been solved at 3.2 Å resolution. The β subunit contains a Zn2+-binding domain, suggesting the ability to bind to DNA . It was then shown that the enzyme is indeed able to bind DNA nonspecifically, and that DNA binding inhibits enzymatic activity . The Zn2+-binding domain of AccD is required both for catalytic activity and for binding to mRNA; the enzyme has higher specificity to mRNA and binds to the coding regions of accA and accD mRNA, inhibiting their translation . Because substrate binding and nucleotide binding appear to be mutually exclusive, the enzyme is able to regulate its own production and catalytic activity . Review:

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN0-5055|reaction.ecocyc.RXN0-5055]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_component_of` --> [[complex.ecocyc.ACETYL-COA-CARBOXYLMULTI-CPLX|complex.ecocyc.ACETYL-COA-CARBOXYLMULTI-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1

## Incoming Edges (2)

- `is_component_of` <-- [[protein.P0A9Q5|protein.P0A9Q5]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` <-- [[protein.P0ABD5|protein.P0ABD5]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:ACETYL-COA-CARBOXYLTRANSFER-CPLX`
- `PDB:2F9Y`
- `PDB:2F9Y`
- `QSPROTEOME:QS00213224`

## Notes

2*protein.P0ABD5|2*protein.P0A9Q5
