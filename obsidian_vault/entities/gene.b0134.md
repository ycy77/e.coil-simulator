---
entity_id: "gene.b0134"
entity_type: "gene"
name: "panB"
source_database: "NCBI RefSeq"
source_id: "gene-b0134"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0134"
  - "panB"
---

# panB

`gene.b0134`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0134`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

panB (gene.b0134) is a gene entity. It encodes panB (protein.P31057). Encoded protein function: FUNCTION: Catalyzes the reversible reaction in which hydroxymethyl group from 5,10-methylenetetrahydrofolate is transferred onto alpha-ketoisovalerate to form ketopantoate. {ECO:0000269|PubMed:6463, ECO:0000269|PubMed:776976}. EcoCyc product frame: 3-CH3-2-OXOBUTANOATE-OH-CH3-XFER-MONOMER. Genomic coordinates: 148807-149601. EcoCyc protein note: 3-methyl-2-oxobutanoate hydroxymethyltransferase (KPHMT, PanB) catalyzes the first committed step of the pantothenate biosynthesis pathway, transferring the C11 carbon of 5,10-methylene-tetrahydrofolate onto 2-keto-isovalerate to form 2-dehydropantoate . 2-Dehydropantoate is an essential precursor of pantothenate . A crystal structure of the enzyme in complex with ketopantoate has been solved at 1.9Å resolution. The enzyme is a member of the (βα)8-barrel superfamily of enzymes; the quarternary structure can best be described as a pentamer of dimers . Comparative genomics has suggested a functional association between PanB and H2PTERIDINEPYROPHOSPHOKIN-MONOMER FolK. The proposed hypothesis is that a side reaction catalyzed by PanB damages 5,10-methylenetetrahydrofolate (CH2-THF), and FolK subsequently recycles the resulting pterin moiety to folate...

## Enriched Pathways

- `eco00770` Pantothenate and CoA biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P31057|protein.P31057]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0000467,ECOCYC:EG11675,GeneID:944839`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:148807-149601:-; feature_type=gene
