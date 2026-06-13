---
entity_id: "protein.P00903"
entity_type: "protein"
name: "pabA"
source_database: "UniProt"
source_id: "P00903"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pabA b3360 JW3323"
---

# pabA

`protein.P00903`

## Static

- Type: `protein`
- Source: `UniProt:P00903`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Part of a heterodimeric complex that catalyzes the two-step biosynthesis of 4-amino-4-deoxychorismate (ADC), a precursor of p-aminobenzoate (PABA) and tetrahydrofolate. In the first step, a glutamine amidotransferase (PabA) generates ammonia as a substrate that, along with chorismate, is used in the second step, catalyzed by aminodeoxychorismate synthase (PabB) to produce ADC. PabA converts glutamine into glutamate only in the presence of stoichiometric amounts of PabB. {ECO:0000269|PubMed:4914080, ECO:0000269|PubMed:7592344}. PabA (component 2) provides the glutamine amidotransferase activity of the aminodeoxychorismate synthase complex . PabA functions as a glutaminase, but only when in complex with PabB . The reaction proceeds via formation of a covalent PabA-γ-glutamyl intermediate . Titration of PabA with PabB showed a gain of glutaminase activity that reached a plateau at a 1:1 ratio of PabA/PabB, suggesting that the effect of PabB is as a stoichiometric positive allosteric effector on the PabA subunit . The presence of chorismate allosterically stimulates the glutaminase activity of PabA further . Analysis of PabA by site-directed mutagenesis suggested a role for the conserved Cys79, His168 and Glu170 as part of the catalytic triad...

## Biological Role

Catalyzes L-glutamine amidohydrolase (reaction.R00256). Component of 4-amino-4-deoxychorismate synthase (complex.ecocyc.PABASYN-CPLX).

## Enriched Pathways

- `eco00790` Folate biosynthesis (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Part of a heterodimeric complex that catalyzes the two-step biosynthesis of 4-amino-4-deoxychorismate (ADC), a precursor of p-aminobenzoate (PABA) and tetrahydrofolate. In the first step, a glutamine amidotransferase (PabA) generates ammonia as a substrate that, along with chorismate, is used in the second step, catalyzed by aminodeoxychorismate synthase (PabB) to produce ADC. PabA converts glutamine into glutamate only in the presence of stoichiometric amounts of PabB. {ECO:0000269|PubMed:4914080, ECO:0000269|PubMed:7592344}.

## Pathways

- `eco00790` Folate biosynthesis (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00256|reaction.R00256]] `KEGG` `database` - via EC:2.6.1.85
- `is_component_of` --> [[complex.ecocyc.PABASYN-CPLX|complex.ecocyc.PABASYN-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b3360|gene.b3360]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P00903`
- `KEGG:ecj:JW3323;eco:b3360;ecoc:C3026_18250;`
- `GeneID:75206304;947873;`
- `GO:GO:0000162; GO:0008153; GO:0009356; GO:0046654; GO:0046656; GO:0046820; GO:0046982`
- `EC:2.6.1.85`

## Notes

Aminodeoxychorismate synthase component 2 (ADC synthase) (ADCS) (EC 2.6.1.85) (4-amino-4-deoxychorismate synthase component 2) (Aminodeoxychorismate synthase, glutamine amidotransferase component)
