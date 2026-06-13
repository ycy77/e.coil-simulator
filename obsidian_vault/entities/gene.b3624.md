---
entity_id: "gene.b3624"
entity_type: "gene"
name: "waaZ"
source_database: "NCBI RefSeq"
source_id: "gene-b3624"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3624"
  - "waaZ"
---

# waaZ

`gene.b3624`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3624`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

waaZ (gene.b3624) is a gene entity. It encodes waaZ (protein.P27241). Encoded protein function: FUNCTION: Involved in the biosynthesis of the core oligosaccharide region of lipopolysaccharide (LPS) (PubMed:12591884). Required for the addition of 3-deoxy-D-manno-oct-2-ulosonic acid III (KdoIII) to the KdoII residue of the inner lipopolysaccharide core (PubMed:12591884). May also play a role in a lipooligosaccharide (LOS) biosynthesis pathway (PubMed:1385388). {ECO:0000269|PubMed:12591884, ECO:0000269|PubMed:1385388}. EcoCyc product frame: EG11426-MONOMER. EcoCyc synonyms: rfaZ. Genomic coordinates: 3799345-3800196. EcoCyc protein note: The lipopolysaccharide of E. coli K-12 consists of two major components: the hydrophobic lipid A moiety inserted into the outer membrane and the phosphorylated core oligosaccharide . E. coli K-12 does not produce O antigen to attach to the LPS core due to a defect in the rfb gene cluster which can be complemented with genes from a second, independent rfb mutant to produce an O16 type O antigen . E. coli K-12 may have two major pathways for LPS biosynthesis. One generates LPS cores suitable for O antigen attachment, and a second generates lipooligosaccharides (LOS) with modifications to the core structure which prevent O antigen attachment...

## Biological Role

Activated by rpoD (protein.P00579), soxS (protein.P0A9E2), marA (protein.P0ACH5).

## Enriched Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P27241|protein.P27241]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=waaZ; function=+
- `activates` <-- [[protein.P0A9E2|protein.P0A9E2]] `RegulonDB` `S` - regulator=SoxS; target=waaZ; function=+
- `activates` <-- [[protein.P0ACH5|protein.P0ACH5]] `RegulonDB` `S` - regulator=MarA; target=waaZ; function=+

## External IDs

- `Dbxref:ASAP:ABE-0011854,ECOCYC:EG11426,GeneID:948146`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3799345-3800196:-; feature_type=gene
