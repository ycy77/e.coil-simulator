---
entity_id: "gene.b1182"
entity_type: "gene"
name: "hlyE"
source_database: "NCBI RefSeq"
source_id: "gene-b1182"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1182"
  - "hlyE"
---

# hlyE

`gene.b1182`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1182`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hlyE (gene.b1182) is a gene entity. It encodes hlyE (protein.P77335). Encoded protein function: FUNCTION: Toxin, which has some hemolytic activity towards mammalian cells. Acts by forming a pore-like structure upon contact with mammalian cells. {ECO:0000269|PubMed:14532000}. EcoCyc product frame: G6619-MONOMER. EcoCyc synonyms: ycgD, clyA, hpr, sheA. Genomic coordinates: 1229483-1230394. EcoCyc protein note: hlyE (also known as clyA or sheA) encodes a secreted, pore-forming protein (hemolysin E/cytolysin A) that is active against mammalian erythrocytes and other cells; E. coli K-12 does not express hlyE under normal laboratory conditions however a hemolytic phenotype can be induced by experimentally manipulating expression levels (see also ). Secretion of hemolysin E into the medium is independent of its cytolytic activity and is paralleled by transient leakage of periplasmic contents . Hemolysin E may be secreted via a vesicle-mediated transport mechanism; over-expressed hemolysin E is found on the cell surface and in outer-membrane-derived vesicles (OMVs) released from the bacterial cell; these vesicles have higher cytotoxic activity than the purified protein; hemolysin E, isolated from the periplasmic fraction, is largely monomeric but forms an oligomeric pore complex in OMVs (see also )...

## Biological Role

Repressed by fis (protein.P0A6R3), hns (protein.P0ACF8), lrp (protein.P0ACJ0). Activated by slyA (protein.P0A8W2), fnr (protein.P0A9E5), hns (protein.P0ACF8), crp (protein.P0ACJ8).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77335|protein.P77335]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (7)

- `activates` <-- [[protein.P0A8W2|protein.P0A8W2]] `RegulonDB` `S` - regulator=SlyA; target=hlyE; function=+
- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `S` - regulator=FNR; target=hlyE; function=+
- `activates` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `S` - regulator=H-+NS; target=hlyE; function=-+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=hlyE; function=+
- `represses` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=hlyE; function=-
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `S` - regulator=H-+NS; target=hlyE; function=-+
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0003962,ECOCYC:G6619,GeneID:945745`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1229483-1230394:-; feature_type=gene
