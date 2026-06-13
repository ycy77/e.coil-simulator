---
entity_id: "protein.P19323"
entity_type: "protein"
name: "fhlA"
source_database: "UniProt"
source_id: "P19323"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fhlA b2731 JW2701"
---

# fhlA

`protein.P19323`

## Static

- Type: `protein`
- Source: `UniProt:P19323`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Required for induction of expression of the formate dehydrogenase H and hydrogenase-3 structural genes. Also activates expression of hyf operon (encodes the silent hydrogenase-4 gene cluster) (PubMed:12426353). {ECO:0000269|PubMed:12426353}.

## Biological Role

Component of FhlA-formate DNA-binding transcriptional activator (complex.ecocyc.MONOMER0-183).

## Annotation

FUNCTION: Required for induction of expression of the formate dehydrogenase H and hydrogenase-3 structural genes. Also activates expression of hyf operon (encodes the silent hydrogenase-4 gene cluster) (PubMed:12426353). {ECO:0000269|PubMed:12426353}.

## Outgoing Edges (19)

- `activates` --> [[gene.b2712|gene.b2712]] `RegulonDB` `S` - regulator=FhlA; target=hypF; function=+
- `activates` --> [[gene.b2713|gene.b2713]] `RegulonDB` `S` - regulator=FhlA; target=hydN; function=+
- `activates` --> [[gene.b2717|gene.b2717]] `RegulonDB` `S` - regulator=FhlA; target=hycI; function=+
- `activates` --> [[gene.b2718|gene.b2718]] `RegulonDB` `S` - regulator=FhlA; target=hycH; function=+
- `activates` --> [[gene.b2719|gene.b2719]] `RegulonDB` `S` - regulator=FhlA; target=hycG; function=+
- `activates` --> [[gene.b2720|gene.b2720]] `RegulonDB` `S` - regulator=FhlA; target=hycF; function=+
- `activates` --> [[gene.b2721|gene.b2721]] `RegulonDB` `S` - regulator=FhlA; target=hycE; function=+
- `activates` --> [[gene.b2722|gene.b2722]] `RegulonDB` `S` - regulator=FhlA; target=hycD; function=+
- `activates` --> [[gene.b2723|gene.b2723]] `RegulonDB` `S` - regulator=FhlA; target=hycC; function=+
- `activates` --> [[gene.b2724|gene.b2724]] `RegulonDB` `S` - regulator=FhlA; target=hycB; function=+
- `activates` --> [[gene.b2725|gene.b2725]] `RegulonDB` `S` - regulator=FhlA; target=hycA; function=+
- `activates` --> [[gene.b2726|gene.b2726]] `RegulonDB` `S` - regulator=FhlA; target=hypA; function=+
- `activates` --> [[gene.b2727|gene.b2727]] `RegulonDB` `S` - regulator=FhlA; target=hypB; function=+
- `activates` --> [[gene.b2728|gene.b2728]] `RegulonDB` `S` - regulator=FhlA; target=hypC; function=+
- `activates` --> [[gene.b2729|gene.b2729]] `RegulonDB` `S` - regulator=FhlA; target=hypD; function=+
- `activates` --> [[gene.b2730|gene.b2730]] `RegulonDB` `S` - regulator=FhlA; target=hypE; function=+
- `activates` --> [[gene.b2731|gene.b2731]] `RegulonDB` `S` - regulator=FhlA; target=fhlA; function=+
- `activates` --> [[gene.b4079|gene.b4079]] `RegulonDB` `S` - regulator=FhlA; target=fdhF; function=+
- `is_component_of` --> [[complex.ecocyc.MONOMER0-183|complex.ecocyc.MONOMER0-183]] `EcoCyc` `database` - EcoCyc component coefficient=

## Incoming Edges (1)

- `encodes` <-- [[gene.b2731|gene.b2731]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P19323`
- `KEGG:ecj:JW2701;eco:b2731;ecoc:C3026_15025;`
- `GeneID:947181;`
- `GO:GO:0000160; GO:0000987; GO:0001216; GO:0005524; GO:0005667; GO:0006351; GO:0032993; GO:0042802; GO:0045893; GO:2000144`

## Notes

Formate hydrogenlyase transcriptional activator FhlA
