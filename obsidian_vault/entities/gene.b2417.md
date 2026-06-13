---
entity_id: "gene.b2417"
entity_type: "gene"
name: "crr"
source_database: "NCBI RefSeq"
source_id: "gene-b2417"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2417"
  - "crr"
---

# crr

`gene.b2417`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2417`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

crr (gene.b2417) is a gene entity. It encodes crr (protein.P69783). Encoded protein function: FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane (PubMed:17158705, PubMed:3129430). The enzyme II complex composed of PtsG and Crr is involved in glucose transport (PubMed:2657735). The non-phosphorylated EIII-Glc is an inhibitor for uptake of certain sugars such as maltose, melibiose, lactose, and glycerol. Phosphorylated EIII-Glc, however, may be an activator for adenylate cyclase. It is an important regulatory protein for cell metabolism (PubMed:789369). {ECO:0000269|PubMed:2657735, ECO:0000269|PubMed:3129430, ECO:0000269|PubMed:789369, ECO:0000305|PubMed:17158705}. EcoCyc product frame: CRR-MONOMER. EcoCyc synonyms: treD, gsr, iex, tgs. Genomic coordinates: 2535834-2536343. EcoCyc protein note: EIIAGlc is an intermediate phosphotransfer protein in the uptake and phosphorylation of glucose , N-acetylmuramic acid and trehalose and also probably interacts with MalX - a PTS permease whose physiological substrate is unclear . EIIAGlc accepts a phosphoryl group from PTSH-MONOMER "PtsH" and transfers it to the the EIIB domain of the sugar PTS permeases...

## Biological Role

Repressed by crp (protein.P0ACJ8), cra (protein.P0ACP1), mlc (protein.P50456). Activated by rpoD (protein.P00579), crp (protein.P0ACJ8), cra (protein.P0ACP1), rpoH (protein.P0AGB3).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P69783|protein.P69783]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (7)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=crr; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=crr; function=-+
- `activates` <-- [[protein.P0ACP1|protein.P0ACP1]] `RegulonDB` `C` - regulator=Cra; target=crr; function=-+
- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=crr; function=+
- `represses` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=crr; function=-+
- `represses` <-- [[protein.P0ACP1|protein.P0ACP1]] `RegulonDB` `C` - regulator=Cra; target=crr; function=-+
- `represses` <-- [[protein.P50456|protein.P50456]] `RegulonDB` `S` - regulator=Mlc; target=crr; function=-

## External IDs

- `Dbxref:ASAP:ABE-0007971,ECOCYC:EG10165,GeneID:946880`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2535834-2536343:+; feature_type=gene
