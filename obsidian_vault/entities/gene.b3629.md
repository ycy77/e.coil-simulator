---
entity_id: "gene.b3629"
entity_type: "gene"
name: "waaS"
source_database: "NCBI RefSeq"
source_id: "gene-b3629"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3629"
  - "waaS"
---

# waaS

`gene.b3629`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3629`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

waaS (gene.b3629) is a gene entity. It encodes waaS (protein.P27126). Encoded protein function: FUNCTION: Probably involved in the biosynthesis of the core oligosaccharide region of lipopolysaccharide (LPS) (PubMed:1385388). May be necessary for the attachment of a rhamnose to the LPS core by a linkage to the KdoII residue (Probable). May also play a role in a lipooligosaccharide (LOS) biosynthesis pathway (PubMed:1385388, PubMed:8444813). {ECO:0000269|PubMed:1385388, ECO:0000269|PubMed:8444813, ECO:0000305|PubMed:9791168}. EcoCyc product frame: EG11350-MONOMER. EcoCyc synonyms: rfaS. Genomic coordinates: 3804181-3805116. EcoCyc protein note: The lipopolysaccharide of E. coli K-12 consists of two major components: the hydrophobic lipid A moiety inserted into the outer membrane and the phosphorylated core oligosaccharide . E. coli K-12 does not produce O antigen to attach to the LPS core due to a defect in the rfb gene cluster which can be complemented with genes from a second, independent rfb mutant to produce an O16 type O antigen . E. coli K-12 may have two major pathways for LPS biosynthesis. One generates LPS cores suitable for O antigen attachment, and a second generates lipooligosaccharides (LOS) with modifications to the core structure which prevent O antigen attachment...

## Biological Role

Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P27126|protein.P27126]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `C` - sigma=sigma70; target=waaS; function=+

## External IDs

- `Dbxref:ASAP:ABE-0011864,ECOCYC:EG11350,GeneID:948151`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3804181-3805116:-; feature_type=gene
