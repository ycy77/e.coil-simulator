---
entity_id: "protein.P24169"
entity_type: "protein"
name: "speF"
source_database: "UniProt"
source_id: "P24169"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "speF b0693 JW0680"
---

# speF

`protein.P24169`

## Static

- Type: `protein`
- Source: `UniProt:P24169`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: The first enzyme leading to putrescine and thus polyamine synthesis. {ECO:0000305}. E. coli encodes two ornithine decarboxylase enzymes, the biosynthetic (constitutive) ORNDECARBOX-BIO-CPLX SpeC and the degradative (inducible) SpeF . SpeF is activated by the guanosine nucleotides GTP, GDP, pppGpp and ppGpp . SpeF enzymatic activity is induced by growth at low pH (5.5) . SpeF is overproduced from a speF-containing plasmid when cells are grown at pH 5.2, but not at pH 7 . Overexpression of RNase III from a plasmid increases expression from the speF promoter, perhaps by processing of the 5' UTR . Expression of SpeF is also regulated by attenuation in response to ornithine ; see the summary for the MONOMER0-4532.

## Biological Role

Catalyzes L-ornithine carboxy-lyase (putrescine-forming) (reaction.R00670). Component of inducible ornithine decarboxylase (complex.ecocyc.ORNDECARBOXDEG-CPLX).

## Enriched Pathways

- `eco00330` Arginine and proline metabolism (KEGG)
- `eco00480` Glutathione metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

FUNCTION: The first enzyme leading to putrescine and thus polyamine synthesis. {ECO:0000305}.

## Pathways

- `eco00330` Arginine and proline metabolism (KEGG)
- `eco00480` Glutathione metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00670|reaction.R00670]] `KEGG` `database` - via EC:4.1.1.17
- `is_component_of` --> [[complex.ecocyc.ORNDECARBOXDEG-CPLX|complex.ecocyc.ORNDECARBOXDEG-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0693|gene.b0693]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P24169`
- `KEGG:ecj:JW0680;eco:b0693;ecoc:C3026_03455;`
- `GeneID:945297;`
- `GO:GO:0004586; GO:0005829; GO:0008295; GO:0030170; GO:0033387; GO:0042803; GO:0071468`
- `EC:4.1.1.17`

## Notes

Inducible ornithine decarboxylase (EC 4.1.1.17)
