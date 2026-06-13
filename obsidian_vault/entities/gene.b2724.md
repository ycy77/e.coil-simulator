---
entity_id: "gene.b2724"
entity_type: "gene"
name: "hycB"
source_database: "NCBI RefSeq"
source_id: "gene-b2724"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2724"
  - "hycB"
---

# hycB

`gene.b2724`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2724`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hycB (gene.b2724) is a gene entity. It encodes hycB (protein.P0AAK1). Encoded protein function: FUNCTION: Probable electron transfer protein for hydrogenase 3. EcoCyc product frame: HYCBSMALL-MONOMER. EcoCyc synonyms: hevB. Genomic coordinates: 2849238-2849849. EcoCyc protein note: The hycBCDEFG genes in E. coli K-12 encode the hydrogenase component (hydrogenase 3) of the formate hydrogenlyase (FHL) complex. HycB is believed to be a peptide of the [4Fe-4S] ferredoxin type, which functions as an intermediate electron carrier protein between the site of formate oxidation in FdhF and the site of H2 production in HycE; HycB is predicted to contain four [4Fe-4S] clusters . In the cryo-EM structures of FHL reported by , HycB interacts with FdhF, HycF, and HycE; an electron-relay containing eight [4Fe-4S] clusters connects the site of formate oxidation and H2 production. A hycB deletion mutant loses molecular hydrogen production and 2H+/K+ exchange abilities under anaerobic glucose-fermenting conditions. It is suggested that HycB is part of the formate-hydrogen lyase complex that interacts directly with the F0F1 ATPase complex and the TrkA system .

## Biological Role

Activated by modE (protein.P0A9G8), fhlA (protein.P19323), rpoN (protein.P24255), ygfI (protein.P52044).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AAK1|protein.P0AAK1]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P0A9G8|protein.P0A9G8]] `RegulonDB` `S` - regulator=ModE; target=hycB; function=+
- `activates` <-- [[protein.P19323|protein.P19323]] `RegulonDB` `S` - regulator=FhlA; target=hycB; function=+
- `activates` <-- [[protein.P24255|protein.P24255]] `RegulonDB` `S` - sigma=sigma54; target=hycB; function=+
- `activates` <-- [[protein.P52044|protein.P52044]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0008950,ECOCYC:EG10475,GeneID:948002`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2849238-2849849:-; feature_type=gene
