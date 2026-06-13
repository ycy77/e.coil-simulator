---
entity_id: "protein.P77589"
entity_type: "protein"
name: "mhpT"
source_database: "UniProt"
source_id: "P77589"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:23934492}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mhpT orfT yaiK b0353 JW5046"
---

# mhpT

`protein.P77589`

## Static

- Type: `protein`
- Source: `UniProt:P77589`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:23934492}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Uptake of 3-(3-hydroxyphenyl)propionate (3HPP) across the cytoplasmic membrane (PubMed:23934492). Transport is driven by the proton motive force (PubMed:23934492). Does not transport benzoate, 3-hydroxybenzoate or gentisate (PubMed:23934492). {ECO:0000269|PubMed:23934492}. MhpT is a putative 3-hydroxyphenylpropionic acid transporter. The mhpT gene is located immediately downstream of the mhpA-E operon, responsible for catabolism of 3-hydroxyphenylpropionate . MhpT is a member of the major facilitator superfamily of transporters and shares a high degree of sequence similarity with PcaK, a 4-hydroxybenzoate transporter from Pseudomonas putida . MhpT may function as a 3-hydroxyphenylpropionate/proton symporter. Imported 3-hydroxyphenylpropionate is converted to 2,3-dihydroxyphenylpropionate and ultimately degraded to Krebs cycle intermediates. MhpT has been implicated in arabinose efflux .

## Biological Role

Catalyzes 3-(3-hydroxyphenyl)propanoate:proton symport (reaction.ecocyc.TRANS-RXN-61), 3-hydroxycinnamate:proton symport (reaction.ecocyc.TRANS-RXN0-457). Transports 3-(3-Hydroxyphenyl)propanoic acid (molecule.C11457), trans-3-Hydroxycinnamate (molecule.C12621), hν (molecule.ecocyc.Light).

## Annotation

FUNCTION: Uptake of 3-(3-hydroxyphenyl)propionate (3HPP) across the cytoplasmic membrane (PubMed:23934492). Transport is driven by the proton motive force (PubMed:23934492). Does not transport benzoate, 3-hydroxybenzoate or gentisate (PubMed:23934492). {ECO:0000269|PubMed:23934492}.

## Outgoing Edges (5)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-61|reaction.ecocyc.TRANS-RXN-61]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-457|reaction.ecocyc.TRANS-RXN0-457]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C11457|molecule.C11457]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C12621|molecule.C12621]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b0353|gene.b0353]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77589`
- `KEGG:ecj:JW5046;eco:b0353;ecoc:C3026_01740;ecoc:C3026_24900;`
- `GeneID:944997;`
- `GO:GO:0005886; GO:0015540; GO:0016020; GO:0042920`

## Notes

3-(3-hydroxy-phenyl)propionate transporter (3HPP transporter) (3-(3-hydroxy-phenyl)propionate:H(+) symporter) (3HPP:H(+) symporter)
