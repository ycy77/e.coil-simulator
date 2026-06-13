---
entity_id: "protein.P31434"
entity_type: "protein"
name: "yicI"
source_database: "UniProt"
source_id: "P31434"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yicI b3656 JW3631"
---

# yicI

`protein.P31434`

## Static

- Type: `protein`
- Source: `UniProt:P31434`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Can catalyze the transfer of alpha-xylosyl residue from alpha-xyloside to xylose, glucose, mannose, fructose, maltose, isomaltose, nigerose, kojibiose, sucrose and trehalose. {ECO:0000269|PubMed:15294295, ECO:0000269|PubMed:15501829}. YicI is a member of the glycosyl hydrolase 31 family and has α-xylosidase activity. The enzyme is specific for α-xyloside linkages and is most active with α-xylosyl fluoride as the substrate, with a Km of 0.17 mM . YicI hydrolyzes p-nitrophenyl α-D-xylopyranoside and α-D-xylopyranosyl fluoride rapidly . YicI can also catalyze transxylosylation, providing information on the substrate interactions at the aglycone binding site. The enzyme prefers aldopyranosyl sugars with an equatorial 4-OH as the acceptor substrate . Site-directed mutagenesis, introducing the C307I and F308D substitutions, changed the substrate specificity of the enzyme from an α-xylosidase to an α-glucosidase . Crystal structures of free YicI and a reaction intermediate and with a nonhydrolyzable substrate analog have been solved. yicJI is predicted to be a member of the EG20253-MONOMER "XylR" regulon; putative XylR and CRP binding sites are identified upstream of yicJI . The yicJI operon appears to be involved in fitness of the pathogenic E. coli strain BEN2908 . Review:

## Biological Role

Component of α-D-xyloside xylohydrolase (complex.ecocyc.CPLX0-3901).

## Annotation

FUNCTION: Can catalyze the transfer of alpha-xylosyl residue from alpha-xyloside to xylose, glucose, mannose, fructose, maltose, isomaltose, nigerose, kojibiose, sucrose and trehalose. {ECO:0000269|PubMed:15294295, ECO:0000269|PubMed:15501829}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3901|complex.ecocyc.CPLX0-3901]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## Incoming Edges (1)

- `encodes` <-- [[gene.b3656|gene.b3656]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P31434`
- `KEGG:ecj:JW3631;eco:b3656;ecoc:C3026_19805;`
- `GeneID:948169;`
- `GO:GO:0005975; GO:0030246; GO:0042802; GO:0061634; GO:0080176`
- `EC:3.2.1.177`

## Notes

Alpha-xylosidase (EC 3.2.1.177)
