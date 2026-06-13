---
entity_id: "protein.P76425"
entity_type: "protein"
name: "rcnA"
source_database: "UniProt"
source_id: "P76425"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15805538}; Multi-pass membrane protein {ECO:0000269|PubMed:15805538}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rcnA yohM b2106 JW2093"
---

# rcnA

`protein.P76425`

## Static

- Type: `protein`
- Source: `UniProt:P76425`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15805538}; Multi-pass membrane protein {ECO:0000269|PubMed:15805538}.

## Enriched Summary

FUNCTION: Efflux system for nickel and cobalt. {ECO:0000269|PubMed:15805538}. RcnA is an inner membrane efflux system for nickel and cobalt ions. Under aerobic growth conditions deletion of rcnA results in decreased resistance to nickel and cobalt and increased intracellular accumulation of Ni2+ can be directly demonstrated . rcnA expressed in trans in a strain lacking chromosomal rcnA results in increased resistance to Ni2+ and Co2+ compared to wild type . RcnA is involved in Ni2+ homeostasis under anaerobic conditions and at low nickel concentrations (10nM Ni2+). Under these conditions deletion of rcnA results in reduced nickel accumulation and decreased HYDROG3-CPLX activity. Deletion of rcnA results in increased EG11519-MONOMER "NikR" activity which impacts nickel import via the high affinity ABC-20-CPLX . RcnA contains 6 predicted transmembrane regions and a histidine rich domain in the center of the protein that may be associated with nickel binding Exposure of rcnA mutants to subinhibitory concentrations of nickel promotes the formation of biofilm structure . rcnA expression is regulated by the G7137-MONOMER "RcnR transcritional repressor" .rcnA forms an operon with G7139-MONOMER "rcnB" . RcnA is a member of the Nickel-Cobalt (NicO) family of transporters .

## Biological Role

Catalyzes Ni2+ export (reaction.ecocyc.TRANS-RXN0-584), Co2+ export (reaction.ecocyc.TRANS-RXN0-585). Transports CO2 (molecule.C00011), Nickel(2+) (molecule.C19609).

## Annotation

FUNCTION: Efflux system for nickel and cobalt. {ECO:0000269|PubMed:15805538}.

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-584|reaction.ecocyc.TRANS-RXN0-584]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-585|reaction.ecocyc.TRANS-RXN0-585]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C19609|molecule.C19609]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b2106|gene.b2106]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76425`
- `KEGG:ecj:JW2093;eco:b2106;ecoc:C3026_11815;`
- `GeneID:949078;`
- `GO:GO:0005886; GO:0006824; GO:0010045; GO:0015099; GO:0032025; GO:0035444; GO:0035785`

## Notes

Nickel/cobalt efflux system RcnA
