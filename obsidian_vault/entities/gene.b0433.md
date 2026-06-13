---
entity_id: "gene.b0433"
entity_type: "gene"
name: "ampG"
source_database: "NCBI RefSeq"
source_id: "gene-b0433"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0433"
  - "ampG"
---

# ampG

`gene.b0433`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0433`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ampG (gene.b0433) is a gene entity. It encodes ampG (protein.P0AE16). Encoded protein function: FUNCTION: Permease involved in cell wall peptidoglycan recycling (PubMed:12426329, PubMed:8878601). Transports, from the periplasm into the cytoplasm, the disaccharide N-acetylglucosaminyl-beta-1,4-anhydro-N-acetylmuramic acid (GlcNAc-anhMurNAc) and GlcNAc-anhMurNAc-peptides (PubMed:12426329). Transport is dependent on the proton motive force (PubMed:12426329). AmpG is also involved in beta-lactamase induction (PubMed:7773404). {ECO:0000269|PubMed:12426329, ECO:0000269|PubMed:7773404, ECO:0000269|PubMed:8878601}. EcoCyc product frame: AMPG-MONOMER. Genomic coordinates: 452070-453545. EcoCyc protein note: AmpG encodes an anhyhyro-muropeptide transporter required for peptidoglycan recycling. In many enterobacteria (but not E. coli) AmpG participates in an EG10040-MONOMER AmpC induction pathway (see ). ampG is required for the induction of β-lactam resistance in an E. coli strain engineered for inducible β-lactamase activity (strain SN0301/pNU305) . ampG mutants are defective in peptidoglycan recycling and release muropeptides (GlnNAc-anhydoMurNAc-tetrapeptide and tetrapeptide) into the culture medium; AmpG is a muropeptide-specific permease required for peptidoglycan recycling (see also...

## Biological Role

Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco01501` beta-Lactam resistance (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AE16|protein.P0AE16]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ampG; function=+

## External IDs

- `Dbxref:ASAP:ABE-0001501,ECOCYC:EG12183,GeneID:946438`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:452070-453545:-; feature_type=gene
