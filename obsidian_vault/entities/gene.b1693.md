---
entity_id: "gene.b1693"
entity_type: "gene"
name: "aroD"
source_database: "NCBI RefSeq"
source_id: "gene-b1693"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1693"
  - "aroD"
---

# aroD

`gene.b1693`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1693`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

aroD (gene.b1693) is a gene entity. It encodes aroD (protein.P05194). Encoded protein function: FUNCTION: Involved in the third step of the chorismate pathway, which leads to the biosynthesis of aromatic amino acids (AroAA). Catalyzes the cis-dehydration of 3-dehydroquinate (DHQ) and introduces the first double bond of the aromatic ring to yield 3-dehydroshikimate. The reaction involves the formation of an imine intermediate between the keto group of 3-dehydroquinate and the epsilon-amino group of a Lys-170 at the active site. {ECO:0000255|HAMAP-Rule:MF_00214, ECO:0000269|PubMed:13198937, ECO:0000269|PubMed:2950851, ECO:0000269|PubMed:3541912, ECO:0000269|PubMed:7592767}. EcoCyc product frame: AROD-MONOMER. Genomic coordinates: 1774686-1775444. EcoCyc protein note: 3-Dehydroquinate dehydratase (DHQ dehydratase) is involved in the 3rd step of the chorismate pathway, which leads to the biosynthesis of aromatic amino acids. DHQ dehydratase catalyzes the conversion of DHQ to 3-dehydroshikimate and introduces the first double bond of the aromatic ring . The first step of the 3-dehydroquinase reaction involves the formation of an imine intermediate between the keto group of 3-dehydroquinate and the e-amino group of a lysine at the active site of the enzyme. Chemical modification and mutagenesis experiments have identified this lysine to be Lys-170...

## Biological Role

Repressed by nac (protein.Q47005). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P05194|protein.P05194]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=aroD; function=+
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=aroD; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0005653,ECOCYC:EG10076,GeneID:946210`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1774686-1775444:+; feature_type=gene
