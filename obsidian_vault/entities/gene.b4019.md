---
entity_id: "gene.b4019"
entity_type: "gene"
name: "metH"
source_database: "NCBI RefSeq"
source_id: "gene-b4019"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4019"
  - "metH"
---

# metH

`gene.b4019`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4019`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

metH (gene.b4019) is a gene entity. It encodes metH (protein.P13009). Encoded protein function: FUNCTION: Catalyzes the transfer of a methyl group from methyl-cobalamin to homocysteine, yielding enzyme-bound cob(I)alamin and methionine. Subsequently, remethylates the cofactor using methyltetrahydrofolate. {ECO:0000269|PubMed:8652590, ECO:0000269|PubMed:9201956}. EcoCyc product frame: HOMOCYSMETB12-MONOMER. Genomic coordinates: 4223828-4227511. EcoCyc protein note: Cobalamin-dependent methionine synthase (MetH) is a large modular protein that catalyzes the transfer of a methyl group from 5-METHYL-THF-GLU-N 5-methyl-tetrahydrofolate to HOMO-CYS to form MET in the final step of the HOMOSER-METSYN-PWY pathway. The reaction can be catalyzed by either of two transmethylases, HOMOCYSMET-MONOMER MetE or MetH. MetH, described here, is dependent on COB-I-ALAMIN (vitamin B12) as a cofactor, whereas MetE is not. MetH can utilize either the mono- or triglutamate forms of folate, while MetE can use only the triglutamate form . MetE and MetH lack sequence similarity, suggesting that these proteins arose by convergent evolution . MetH is composed of four functionally distinct modules that are arranged linearly with single interdomain linkers. The N-terminal module binds homocysteine, while the second module binds methyl-tetrahydrofolate (methylTHF)...

## Biological Role

Repressed by lrp (protein.P0ACJ0).

## Enriched Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00450` Selenocompound metabolism (KEGG)
- `eco00670` One carbon pool by folate (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)
- `eco04980` Cobalamin transport and metabolism (KEGG)
- `eco04981` Folate transport and metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P13009|protein.P13009]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0013140,ECOCYC:EG10587,GeneID:948522`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4223828-4227511:+; feature_type=gene
