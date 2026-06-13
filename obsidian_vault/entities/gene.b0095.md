---
entity_id: "gene.b0095"
entity_type: "gene"
name: "ftsZ"
source_database: "NCBI RefSeq"
source_id: "gene-b0095"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0095"
  - "ftsZ"
---

# ftsZ

`gene.b0095`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0095`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ftsZ (gene.b0095) is a gene entity. It encodes ftsZ (protein.P0A9A6). Encoded protein function: FUNCTION: Essential cell division protein that forms a contractile ring structure (Z ring) at the future cell division site. The regulation of the ring assembly controls the timing and the location of cell division. One of the functions of the FtsZ ring is to recruit other cell division proteins to the septum to produce a new cell wall between the dividing cells. Binds GTP and shows GTPase activity. Polymerization and bundle formation is enhanced by CbeA. EcoCyc product frame: EG10347-MONOMER. EcoCyc synonyms: sfiB, sulB. Genomic coordinates: 105305-106456. EcoCyc protein note: Assembly of FtsZ into a ring structure (the Z ring, ) at the future cell division site is the earliest known event in cell division. FtsZ is the most highly conserved of the proteins that eventually comprise the septal ring structure; homologs of FtsZ are nearly universally present in bacteria as well as in many archaea, some chloroplasts and a few mitochondria . FtsZ is essential ; it binds GTP and has Mg2+-dependent GTPase activity . Assembly of FtsZ into protein filaments is dynamic and regulated by GTP hydrolysis , resembling tubulin . Turnover of FtsZ within the Z ring is extremely rapid, with the rate-limiting step for turnover likely to be GTP hydrolysis...

## Biological Role

Repressed by ArgR-L-arginine DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-228), dicF (gene.b1574), sdiA (protein.P07026), argR (protein.P0A6D0), pdhR (protein.P0ACL9), mraZ (protein.P22186). Activated by rcsB (protein.P0DMC7), rpoS (protein.P13445).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A9A6|protein.P0A9A6]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (8)

- `activates` <-- [[protein.P0DMC7|protein.P0DMC7]] `RegulonDB` `S` - regulator=RcsB; target=ftsZ; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=ftsZ; function=+
- `represses` <-- [[complex.ecocyc.CPLX0-228|complex.ecocyc.CPLX0-228]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[gene.b1574|gene.b1574]] `RegulonDB` `S` - regulator=DicF; target=ftsZ; function=-
- `represses` <-- [[protein.P07026|protein.P07026]] `RegulonDB` `S` - regulator=SdiA; target=ftsZ; function=-
- `represses` <-- [[protein.P0A6D0|protein.P0A6D0]] `RegulonDB` `S` - regulator=ArgR; target=ftsZ; function=-
- `represses` <-- [[protein.P0ACL9|protein.P0ACL9]] `RegulonDB` `S` - regulator=PdhR; target=ftsZ; function=-
- `represses` <-- [[protein.P22186|protein.P22186]] `RegulonDB` `C` - regulator=MraZ; target=ftsZ; function=-

## External IDs

- `Dbxref:ASAP:ABE-0000333,ECOCYC:EG10347,GeneID:944786`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:105305-106456:+; feature_type=gene
