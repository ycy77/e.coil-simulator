---
entity_id: "gene.b4207"
entity_type: "gene"
name: "fklB"
source_database: "NCBI RefSeq"
source_id: "gene-b4207"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4207"
  - "fklB"
---

# fklB

`gene.b4207`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4207`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fklB (gene.b4207) is a gene entity. It encodes fklB (protein.P0A9L3). Encoded protein function: FUNCTION: PPIases accelerate the folding of proteins (Probable). Catalyzes the cis-trans isomerization of proline imidic peptide bonds in oligopeptides (PubMed:8703024). Displays a preference for substrates with a lysyl residue in the P1 position (PubMed:8703024). {ECO:0000269|PubMed:8703024, ECO:0000305}. EcoCyc product frame: G7865-MONOMER. EcoCyc synonyms: ytfC. Genomic coordinates: 4428935-4429555. EcoCyc protein note: The FklB protein is an FKBP (FK506 binding protein)-type peptidyl-prolyl cis-trans isomerase (PPIase) that may be located in the periplasm. Sequence analysis indicates that FklB is related to the Mip (macrophage infectivity potentiator)-like FKBPs which occur in many intracellular pathogens . Substrates were identified by pull-down assay and include Rob, Crl, PcnB, and ObgE . Purified FklB (from E. coli K-12 HB101) is a dimer in solution; the enzyme shows a preference for substrate with a hydrophobic side chain in position P1 (eg Suc-Ala-Leu-Pro-Phe) and also for a lysyl residue at this position (Suc-Ala-Lys-Pro-Phe); PPIase activity is inhibited in vitro by the immunosuppressive drug FK506...

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A9L3|protein.P0A9L3]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=fklB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0013759,ECOCYC:G7865,GeneID:948726`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4428935-4429555:+; feature_type=gene
