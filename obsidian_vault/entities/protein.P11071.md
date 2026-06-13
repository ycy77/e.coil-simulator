---
entity_id: "protein.P11071"
entity_type: "protein"
name: "aceK"
source_database: "UniProt"
source_id: "P11071"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "aceK b4016 JW3976"
---

# aceK

`protein.P11071`

## Static

- Type: `protein`
- Source: `UniProt:P11071`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Bifunctional enzyme which can phosphorylate or dephosphorylate isocitrate dehydrogenase (IDH) on a specific serine residue. This is a regulatory mechanism which enables bacteria to bypass the Krebs cycle via the glyoxylate shunt in response to the source of carbon. When bacteria are grown on glucose, IDH is fully active and unphosphorylated, but when grown on acetate or ethanol, the activity of IDH declines drastically concomitant with its phosphorylation. Isocitrate dehydrogenase kinase/phosphatase (AceK) controls a branch point between two pathways of central metabolism, the TCA and the GLYOXYLATE-BYPASS, shown in the TCA-GLYOX-BYPASS. It controls the flux between the two cycles by controlling the activity of ISOCITHASE-CPLX (IDH), an enzyme of the TCA cycle . By phosphorylating and thus inactivating IDH , its substrate isocitrate is diverted to the glyoxylate cycle enzyme, isocitrate lyase. By dephosphorylating and thus activating IDH, this enzyme's stronger affinity for isocitrate feeds it into the TCA cycle. Models that attempt to explain the robustness of the IDH regulatory system have been published and have provided potential explanations . Phosphorylation and dephosphorylation of IDH were found to be carried out by the same enzyme, AceK . A conformational switch that is induced by AMP appears to determine whether AceK acts as a kinase or a phosphatase...

## Biological Role

Component of isocitrate dehydrogenase kinase / isocitrate dehydrogenase phosphatase (complex.ecocyc.CPLX0-230).

## Annotation

FUNCTION: Bifunctional enzyme which can phosphorylate or dephosphorylate isocitrate dehydrogenase (IDH) on a specific serine residue. This is a regulatory mechanism which enables bacteria to bypass the Krebs cycle via the glyoxylate shunt in response to the source of carbon. When bacteria are grown on glucose, IDH is fully active and unphosphorylated, but when grown on acetate or ethanol, the activity of IDH declines drastically concomitant with its phosphorylation.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-230|complex.ecocyc.CPLX0-230]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b4016|gene.b4016]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P11071`
- `KEGG:ecj:JW3976;eco:b4016;ecoc:C3026_21695;`
- `GeneID:944797;`
- `GO:GO:0000287; GO:0004674; GO:0004721; GO:0004722; GO:0005524; GO:0005737; GO:0006006; GO:0006097; GO:0006099; GO:0008772; GO:0016208; GO:0030145`
- `EC:2.7.11.5; 3.1.3.-`

## Notes

Isocitrate dehydrogenase kinase/phosphatase (IDH kinase/phosphatase) (IDHK/P) (EC 2.7.11.5) (EC 3.1.3.-)
