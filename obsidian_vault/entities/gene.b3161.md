---
entity_id: "gene.b3161"
entity_type: "gene"
name: "mtr"
source_database: "NCBI RefSeq"
source_id: "gene-b3161"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3161"
  - "mtr"
---

# mtr

`gene.b3161`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3161`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mtr (gene.b3161) is a gene entity. It encodes mtr (protein.P0AAD2). Encoded protein function: FUNCTION: Involved in the transport of tryptophan into the cell. {ECO:0000269|PubMed:4919744, ECO:0000269|PubMed:7814318}. EcoCyc product frame: MTR-MONOMER. Genomic coordinates: 3304573-3305817. EcoCyc protein note: Early studies in E. coli K-12 identified several systems for aromatic amino acid transport including one specific for tryptophan with an apparent Michealis constant of 3 μM . 5-methyl-tryptophan resistant (mtr) mutations described initially by result in loss of this tryptophan-specific transport system (see ). Mtr-mediated tryptophan transport is influenced by the growth medium and Mtr is also able to transport indole although this capability has been disputed . Deletion of mtr negates the indole-induced enhancement of antimicrobial (malachite green) uptake . Membrane topology analysis, together with sequence data, suggests that Mtr contains 11 transmembrane domains with its N-terminus located in the cytoplasm . Expression of mtr is repressed by tryptophan via the CPLX-125 Trp repressor and induced by phenylalanine or tyrosine via PD00413 TyrR . In the Transporter Classification Database () Mtr is a member of the Hydroxy/Aromatic Amino Acid Permease (HAAAP) family within the Amino Acid-Polyamine-Organocation (APC) superfamily...

## Biological Role

Repressed by trpR (protein.P0A881), lrp (protein.P0ACJ0). Activated by rpoD (protein.P00579), tyrR (protein.P07604).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AAD2|protein.P0AAD2]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=mtr; function=+
- `activates` <-- [[protein.P07604|protein.P07604]] `RegulonDB` `C` - regulator=TyrR; target=mtr; function=+
- `represses` <-- [[protein.P0A881|protein.P0A881]] `RegulonDB` `C` - regulator=TrpR; target=mtr; function=-
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB|EcoCyc` `S` - regulator=Lrp; target=mtr; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0010387,ECOCYC:EG10617,GeneID:947675`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3304573-3305817:-; feature_type=gene
