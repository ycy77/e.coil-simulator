---
entity_id: "gene.b0873"
entity_type: "gene"
name: "hcp"
source_database: "NCBI RefSeq"
source_id: "gene-b0873"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0873"
  - "hcp"
---

# hcp

`gene.b0873`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0873`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hcp (gene.b0873) is a gene entity. It encodes hcp (protein.P75825). Encoded protein function: FUNCTION: Catalyzes the reduction of hydroxylamine to form NH(3) and H(2)O. Is also able to reduce hydroxylamine analogs such as methylhydroxylamine and hydroxyquinone. Might have a role as a scavenger of potentially toxic by-products of nitrate metabolism. {ECO:0000255|HAMAP-Rule:MF_00069, ECO:0000269|PubMed:10651802, ECO:0000269|PubMed:12374823}. EcoCyc product frame: G6457-MONOMER. EcoCyc synonyms: priS, ybjW. Genomic coordinates: 912162-913814. EcoCyc protein note: The hybrid cluster protein (HCP) is a high-affinity NO reductase that is responsible for the majority of NO detoxification at low concentrations of NO . HCP exhibits hydroxylamine reductase activity, possibly functioning as a scavenger of toxic by-products of nitrogen metabolism . HCP was originally suggested to be involved in nitrate-and/or nitrite respiration based on its regulation . HCP contains iron-sulfur clusters of the [2Fe-2S] and [4Fe-2S-2O] type and is reduced by the Hcr NADH oxidoreductase . The properties of electron transfer in the Hcr-HCP system have been studied . Growth of an hcp hcr mutant in a strain background that lacks known NO reductases and nitrite reductases (i.e. ΔnirBD, nrfAB, norVW) is inhibited in the presence of nitrate or nitrite...

## Biological Role

Repressed by nsrR (protein.P0AF63). Activated by DNA-binding transcriptional dual regulator CpxR-phosphorylated (complex.ecocyc.CPLX0-7748), fnr (protein.P0A9E5), oxyR (protein.P0ACQ4), narL (protein.P0AF28), rpoE (protein.P0AGB6).

## Enriched Pathways

- `eco00910` Nitrogen metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75825|protein.P75825]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (6)

- `activates` <-- [[complex.ecocyc.CPLX0-7748|complex.ecocyc.CPLX0-7748]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `C` - regulator=FNR; target=hcp; function=+
- `activates` <-- [[protein.P0ACQ4|protein.P0ACQ4]] `RegulonDB` `S` - regulator=OxyR; target=hcp; function=+
- `activates` <-- [[protein.P0AF28|protein.P0AF28]] `RegulonDB` `S` - regulator=NarL; target=hcp; function=+
- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=hcp; function=+
- `represses` <-- [[protein.P0AF63|protein.P0AF63]] `RegulonDB` `C` - regulator=NsrR; target=hcp; function=-

## External IDs

- `Dbxref:ASAP:ABE-0002962,ECOCYC:G6457,GeneID:946592`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:912162-913814:-; feature_type=gene
