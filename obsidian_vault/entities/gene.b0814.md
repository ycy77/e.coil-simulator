---
entity_id: "gene.b0814"
entity_type: "gene"
name: "ompX"
source_database: "NCBI RefSeq"
source_id: "gene-b0814"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0814"
  - "ompX"
---

# ompX

`gene.b0814`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0814`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ompX (gene.b0814) is a gene entity. It encodes ompX (protein.P0A917). Encoded protein function: Outer membrane protein X EcoCyc product frame: EG12117-MONOMER. EcoCyc synonyms: ybiG, ompP. Genomic coordinates: 850450-850965. EcoCyc protein note: OmpX is a small (18 kDa) outer-membrane protein (OMP). Adhesion of E. coli cells to abiotic surfaces via type1 fimbriae leads to a decreased level of OmpX as well as a number of other outer membrane proteins . Deletion of ompX leads to an increase in cell-surface contact in fimbriated strains of E. coli, and production of type 1 fimbriae is upregulated. Furthermore, ompX mutants show impaired motility, increased EPS production, and increased tolerance to SDS and hydrophobic antibiotics. In nonfimbriated strains, deletion of ompX led to a decrease in cell surface contact . OmpX has been implicated in the secretion of the extracellular protein EG11807-MONOMER "YebF" . Expression of OmpX is affected by medium osmolarity and pressure; the effect is independent of EnvZ and OmpR . Both acidic and basic conditions induce OmpX expression . Overproduction of OmpX causes an increase in EσE activity . The OmpX protein shows similarity to a family of outer membrane proteins which are involved in virulence, such as Ail of Yersinia enterocolitica and Rck and PagC of Salmonella typhimurium. However, the OmpX protein of E...

## Biological Role

Repressed by micA (gene.b4442). Activated by DNA-binding transcriptional dual regulator OmpR-phosphorylated (complex.ecocyc.PHOSPHO-OMPR), rpoD (protein.P00579), ompR (protein.P0AA16).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A917|protein.P0A917]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[complex.ecocyc.PHOSPHO-OMPR|complex.ecocyc.PHOSPHO-OMPR]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ompX; function=+
- `activates` <-- [[protein.P0AA16|protein.P0AA16]] `RegulonDB` `S` - regulator=OmpR; target=ompX; function=+
- `represses` <-- [[gene.b4442|gene.b4442]] `RegulonDB` `S` - regulator=MicA; target=ompX; function=-

## External IDs

- `Dbxref:ASAP:ABE-0002784,ECOCYC:EG12117,GeneID:944967`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:850450-850965:+; feature_type=gene
