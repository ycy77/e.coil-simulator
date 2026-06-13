---
entity_id: "protein.P30147"
entity_type: "protein"
name: "hyi"
source_database: "UniProt"
source_id: "P30147"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hyi gip ybbG b0508 JW0496"
---

# hyi

`protein.P30147`

## Static

- Type: `protein`
- Source: `UniProt:P30147`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the reversible isomerization between hydroxypyruvate and 2-hydroxy-3-oxopropanoate (also termed tartronate semialdehyde). Does not catalyze the isomerization of D-fructose to D-glucose or that of D-xylulose to D-xylose. Also does not catalyze racemization of serine, alanine, glycerate or lactate. {ECO:0000269|PubMed:10561547}. Hydroxypyruvate isomerase is a cofactor-independent racemase that catalyzes the reversible isomerization between hydroxypyruvate and tartronate semialdehyde .

## Biological Role

Component of hydroxypyruvate isomerase (complex.ecocyc.CPLX-171).

## Enriched Pathways

- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Catalyzes the reversible isomerization between hydroxypyruvate and 2-hydroxy-3-oxopropanoate (also termed tartronate semialdehyde). Does not catalyze the isomerization of D-fructose to D-glucose or that of D-xylulose to D-xylose. Also does not catalyze racemization of serine, alanine, glycerate or lactate. {ECO:0000269|PubMed:10561547}.

## Pathways

- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX-171|complex.ecocyc.CPLX-171]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0508|gene.b0508]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P30147`
- `KEGG:ecj:JW0496;eco:b0508;ecoc:C3026_02495;`
- `GeneID:946186;`
- `GO:GO:0008903; GO:0042803; GO:0046487`
- `EC:5.3.1.22`

## Notes

Hydroxypyruvate isomerase (EC 5.3.1.22) (Glyoxylate-induced protein)
