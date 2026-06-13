---
entity_id: "gene.b3458"
entity_type: "gene"
name: "livK"
source_database: "NCBI RefSeq"
source_id: "gene-b3458"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3458"
  - "livK"
---

# livK

`gene.b3458`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3458`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

livK (gene.b3458) is a gene entity. It encodes livK (protein.P04816). Encoded protein function: FUNCTION: This protein is a component of the leucine-specific transport system, which is one of the two periplasmic binding protein-dependent transport systems of the high-affinity transport of the branched-chain amino acids in E.coli. EcoCyc product frame: LIVK-MONOMER. EcoCyc synonyms: hrbD, hrbC, hrbB. Genomic coordinates: 3596451-3597560. EcoCyc protein note: LivK is the periplasmic binding protein of the LS or leucine specific ABC transport system in E. coli K-12 . The LS system (LivKHMGF) is able to transport phenylanine and plays a physiologically relevant role in phenylalanine accumulation . The LS system transports both isomers of leucine . LivK is synthesized as a precursor; a 23 amino acid signal sequence is cleaved upon export to the periplasm . Purified LivK* binds L-leucine (apparent KD = 0.4 µM) and L-phenylalanine (apparent KD = 0.18 µM) but does not bind L-isoleucine or L-valine (KD > 1 mM) (LivK* denotes a protein that has been engineered with a StyI restriction site added at codon 124). The crystal structure of LivK in both the apo- and ligand-bound form has been determined at 1.5 and 1.8 A resolution...

## Biological Role

Repressed by nac (protein.Q47005). Activated by rpoD (protein.P00579), lrp (protein.P0ACJ0).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)
- `eco02024` Quorum sensing (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P04816|protein.P04816]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=livK; function=+
- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=livK; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0011292,ECOCYC:EG10540,GeneID:947964`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3596451-3597560:-; feature_type=gene
