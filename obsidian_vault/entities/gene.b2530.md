---
entity_id: "gene.b2530"
entity_type: "gene"
name: "iscS"
source_database: "NCBI RefSeq"
source_id: "gene-b2530"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2530"
  - "iscS"
---

# iscS

`gene.b2530`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2530`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

iscS (gene.b2530) is a gene entity. It encodes iscS (protein.P0A6B7). Encoded protein function: FUNCTION: Master enzyme that delivers sulfur to a number of partners involved in Fe-S cluster assembly, tRNA modification or cofactor biosynthesis. Catalyzes the removal of elemental sulfur from cysteine to produce alanine. Functions as a sulfur delivery protein for Fe-S cluster synthesis onto IscU, an Fe-S scaffold assembly protein, as well as other S acceptor proteins. Preferentially binds to disordered IscU on which the Fe-S is assembled, IscU converts to the structured state and then dissociates from IscS to transfer the Fe-S to an acceptor protein. Also functions as a selenium delivery protein in the pathway for the biosynthesis of selenophosphate. Transfers sulfur onto 'Cys-456' of ThiI and onto 'Cys-19' of TusA in transpersulfidation reactions. {ECO:0000269|PubMed:10544286, ECO:0000269|PubMed:10600118, ECO:0000269|PubMed:10781558, ECO:0000269|PubMed:10781607, ECO:0000269|PubMed:10829016, ECO:0000269|PubMed:10908675, ECO:0000269|PubMed:11577100, ECO:0000269|PubMed:16387657, ECO:0000269|PubMed:22203963, ECO:0000269|PubMed:8663056}. EcoCyc product frame: G7325-MONOMER. EcoCyc synonyms: nuvC, yzzO, yfhO. Genomic coordinates: 2660317-2661531.

## Biological Role

Repressed by ryhB (gene.b4451), iscR (protein.P0AGK8). Activated by oxyS (gene.b4458), rpoD (protein.P00579).

## Enriched Pathways

- `eco00730` Thiamine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)
- `eco04122` Sulfur relay system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A6B7|protein.P0A6B7]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[gene.b4458|gene.b4458]] `RegulonDB` `S` - regulator=OxyS; target=iscS; function=+
- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=iscS; function=+
- `represses` <-- [[gene.b4451|gene.b4451]] `RegulonDB` `S` - regulator=RyhB; target=iscS; function=-
- `represses` <-- [[protein.P0AGK8|protein.P0AGK8]] `RegulonDB` `C` - regulator=IscR; target=iscS; function=-

## External IDs

- `Dbxref:ASAP:ABE-0008324,ECOCYC:G7325,GeneID:947004`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2660317-2661531:-; feature_type=gene
