---
entity_id: "gene.b3656"
entity_type: "gene"
name: "yicI"
source_database: "NCBI RefSeq"
source_id: "gene-b3656"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3656"
  - "yicI"
---

# yicI

`gene.b3656`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3656`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yicI (gene.b3656) is a gene entity. It encodes yicI (protein.P31434). Encoded protein function: FUNCTION: Can catalyze the transfer of alpha-xylosyl residue from alpha-xyloside to xylose, glucose, mannose, fructose, maltose, isomaltose, nigerose, kojibiose, sucrose and trehalose. {ECO:0000269|PubMed:15294295, ECO:0000269|PubMed:15501829}. EcoCyc product frame: EG11685-MONOMER. Genomic coordinates: 3832219-3834537. EcoCyc protein note: YicI is a member of the glycosyl hydrolase 31 family and has α-xylosidase activity. The enzyme is specific for α-xyloside linkages and is most active with α-xylosyl fluoride as the substrate, with a Km of 0.17 mM . YicI hydrolyzes p-nitrophenyl α-D-xylopyranoside and α-D-xylopyranosyl fluoride rapidly . YicI can also catalyze transxylosylation, providing information on the substrate interactions at the aglycone binding site. The enzyme prefers aldopyranosyl sugars with an equatorial 4-OH as the acceptor substrate . Site-directed mutagenesis, introducing the C307I and F308D substitutions, changed the substrate specificity of the enzyme from an α-xylosidase to an α-glucosidase . Crystal structures of free YicI and a reaction intermediate and with a nonhydrolyzable substrate analog have been solved. yicJI is predicted to be a member of the EG20253-MONOMER "XylR" regulon; putative XylR and CRP binding sites are identified upstream of yicJI...

## Biological Role

Activated by rpoE (protein.P0AGB6).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P31434|protein.P31434]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=yicI; function=+

## External IDs

- `Dbxref:ASAP:ABE-0011951,ECOCYC:EG11685,GeneID:948169`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3832219-3834537:-; feature_type=gene
