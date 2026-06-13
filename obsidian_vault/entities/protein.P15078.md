---
entity_id: "protein.P15078"
entity_type: "protein"
name: "cstA"
source_database: "UniProt"
source_id: "P15078"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "cstA ybdC b0598 JW0590"
---

# cstA

`protein.P15078`

## Static

- Type: `protein`
- Source: `UniProt:P15078`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Involved in peptide utilization during carbon starvation. {ECO:0000269|PubMed:1848300}. cstA encodes a specific, moderate affinity pyruvate transporter which mediates the proton-dependent uptake of pyruvate; expression of the transporter from a plasmid enables the growth of a triple mutant strain (ΔG7942 btsT ΔcstA ΔEG12268 yhjX) that is otherwise unable to grow with pyruvate as a sole carbon and energy source . cstA is induced during carbon (succinate, glycerol or glucose) starvation or upon entry into stationary phase; expression is dependent on RPOD-MONOMER σ70 and positively regulated by cAMP-CRP . The growth impairment of cstA opp double null mutants is evident only when peptides serve as carbon and energy source implicating cstA in peptide utilization . cstA expression is negatively regulated by CPLX0-7705 Fis and by CPLX0-7956 CsrA; CsrA binds specifically to cstA mRNA and the interaction is highly cooperative . The inner membrane protein CstA and the small protein MONOMER0-2660 YbdD are implicated in constitutive pyruvate import; cstA and ybdD transposon mutants are enriched in the presence of the toxic pyruvate analog, 3 fluoropyruvate (3FP); ΔcstA and ΔybdD strains avoid 3FP-induced growth inhibition (under pyruvate non-induced conditions) and import significantly less pyruvate than wild-type strains (under pyruvate induced conditions)...

## Biological Role

Catalyzes pyruvate:proton symport (reaction.ecocyc.TRANS-RXN-335).

## Annotation

FUNCTION: Involved in peptide utilization during carbon starvation. {ECO:0000269|PubMed:1848300}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-335|reaction.ecocyc.TRANS-RXN-335]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0598|gene.b0598]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P15078`
- `KEGG:ecj:JW0590;eco:b0598;ecoc:C3026_02985;`
- `GeneID:945213;`
- `GO:GO:0005477; GO:0005886; GO:0006849; GO:0009267; GO:0015031; GO:0015833; GO:0031669`

## Notes

Peptide transporter CstA (Carbon starvation protein A)
