---
entity_id: "gene.b4034"
entity_type: "gene"
name: "malE"
source_database: "NCBI RefSeq"
source_id: "gene-b4034"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4034"
  - "malE"
---

# malE

`gene.b4034`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4034`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

malE (gene.b4034) is a gene entity. It encodes malE (protein.P0AEX9). Encoded protein function: FUNCTION: Part of the ABC transporter complex MalEFGK involved in maltose/maltodextrin import. Binds maltose and higher maltodextrins such as maltotriose. {ECO:0000269|PubMed:2026607, ECO:0000269|PubMed:2155217, ECO:0000269|PubMed:4215651, ECO:0000269|PubMed:776623}. EcoCyc product frame: MALE-MONOMER. Genomic coordinates: 4245229-4246419. EcoCyc protein note: malE encodes the periplasmic substrate-binding component of the maltose ABC transporter. MalE, or maltodextrin binding protein (MBP) can bind linear maltodextrins, cyclic maltodextrins and various maltodextrin analogues although only linear maltodextrins up maltoheptaose are substrates for transport . Non-polar malE deletion mutants do not show appreciable growth on media containing maltose concentrations up to 25 mM . MBP consists of two globular domains separated by a deep groove which contains the maltodextrin binding site. MBP adopts two distinct conformations - an open unliganded form in which the two globular domains are far apart and the binding groove is accessible and a closed liganded structure. Bound maltose is almost completely enclosed and is held in place by hydrogen bonds and Van der Waals interactions...

## Biological Role

Repressed by DNA-binding transcriptional dual regulator OmpR-phosphorylated (complex.ecocyc.PHOSPHO-OMPR), ompR (protein.P0AA16), yidZ (protein.P31463). Activated by rpoD (protein.P00579), malT (protein.P06993), fis (protein.P0A6R3), crp (protein.P0ACJ8).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)
- `eco02030` Bacterial chemotaxis (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AEX9|protein.P0AEX9]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (7)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=malE; function=+
- `activates` <-- [[protein.P06993|protein.P06993]] `RegulonDB` `C` - regulator=MalT; target=malE; function=+
- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=malE; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=malE; function=+
- `represses` <-- [[complex.ecocyc.PHOSPHO-OMPR|complex.ecocyc.PHOSPHO-OMPR]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0AA16|protein.P0AA16]] `RegulonDB` `S` - regulator=OmpR; target=malE; function=-
- `represses` <-- [[protein.P31463|protein.P31463]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0013200,ECOCYC:EG10554,GeneID:948538`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4245229-4246419:-; feature_type=gene
