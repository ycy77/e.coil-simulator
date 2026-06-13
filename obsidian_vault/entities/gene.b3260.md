---
entity_id: "gene.b3260"
entity_type: "gene"
name: "dusB"
source_database: "NCBI RefSeq"
source_id: "gene-b3260"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3260"
  - "dusB"
---

# dusB

`gene.b3260`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3260`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dusB (gene.b3260) is a gene entity. It encodes dusB (protein.P0ABT5). Encoded protein function: FUNCTION: Catalyzes the synthesis of 5,6-dihydrouridine (D), a modified base found in the D-loop of most tRNAs, via the reduction of the C5-C6 double bond in target uridines. {ECO:0000255|HAMAP-Rule:MF_02042, ECO:0000269|PubMed:11983710}. EcoCyc product frame: EG11311-MONOMER. EcoCyc synonyms: yhdG. Genomic coordinates: 3410280-3411245. EcoCyc protein note: DusB and EG12022-MONOMER (DusC) together account for about half of the 5,6-dihydrouridine modification observed in wild-type cellular tRNA, and EG11932-MONOMER (DusA) accounts for the other half . Crystal structure of DusB in complex with a tRNA transcript was obtained showing conservation the Dus fold. Despite some structural similarities DusB was found to have a new uridine binding mechanism not seen previously in the Dus family proteins . A dusA dusB dusC triple mutant exhibits a complete lack of 5,6-dihydrouridine modification in cellular tRNA, whereas each single mutant exhibits a partial reduction, compared to wild type . Using a ΔdusB mutant, the specificity of DusB for dihydrouridylation of nucleotide 17 (D17) was determined in ARG-tRNAs (ICG), ILE-tRNAs (GAU) and LEU-tRNAs (CAG)...

## Biological Role

Repressed by fis (protein.P0A6R3). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ABT5|protein.P0ABT5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `C` - sigma=sigma70; target=dusB; function=+
- `represses` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `C` - regulator=Fis; target=dusB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0010700,ECOCYC:EG11311,GeneID:947707`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3410280-3411245:+; feature_type=gene
