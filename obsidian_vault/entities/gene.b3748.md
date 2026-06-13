---
entity_id: "gene.b3748"
entity_type: "gene"
name: "rbsD"
source_database: "NCBI RefSeq"
source_id: "gene-b3748"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3748"
  - "rbsD"
---

# rbsD

`gene.b3748`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3748`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rbsD (gene.b3748) is a gene entity. It encodes rbsD (protein.P04982). Encoded protein function: FUNCTION: Catalyzes the interconversion of beta-pyran and beta-furan forms of D-ribose. It also catalyzes the conversion between beta-allofuranose and beta-allopyranose. {ECO:0000269|PubMed:15060078}. EcoCyc product frame: EG10817-MONOMER. EcoCyc synonyms: rbsP. Genomic coordinates: 3933351-3933770. EcoCyc protein note: RbsD is a ribose pyranase; it binds specifically to the β-furan and β-pyran forms of ribose and increases the exchange rate between the two forms . A preliminary crystallographic analysis of RbsD was reported, but no structure coordinates were deposited with PDB . Based on analytical centrifugation analysis, RbsD was initially reported to be an octamer in solution ; analysis of the crystal structure showed it to be a decamer, similar to the Bacillus subtilis homolog , while gel permeation chromatography indicated that the protein was a heptamer . Under urea-induced denaturation conditions, the homodecamer undergoes stepwise disassembly and non-stepwise reassembly . The Lys2 residue appears to be involved in stabilization of the oligomeric state . The RbsD protein is required for efficient utilization of ribose when ribose is transported into the cell via a mutated form of PtsG, the glucose transporter. A mutation in rbsD does not abolish ribose transport...

## Biological Role

Repressed by dsrA (gene.b1954), rbsR (protein.P0ACQ0), yidZ (protein.P31463).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P04982|protein.P04982]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `represses` <-- [[gene.b1954|gene.b1954]] `RegulonDB` `S` - regulator=DsrA; target=rbsD; function=-
- `represses` <-- [[protein.P0ACQ0|protein.P0ACQ0]] `RegulonDB` `C` - regulator=RbsR; target=rbsD; function=-
- `represses` <-- [[protein.P31463|protein.P31463]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0012256,ECOCYC:EG10817,GeneID:948267`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3933351-3933770:+; feature_type=gene
