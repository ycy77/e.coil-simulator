---
entity_id: "gene.b3389"
entity_type: "gene"
name: "aroB"
source_database: "NCBI RefSeq"
source_id: "gene-b3389"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3389"
  - "aroB"
---

# aroB

`gene.b3389`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3389`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

aroB (gene.b3389) is a gene entity. It encodes aroB (protein.P07639). Encoded protein function: FUNCTION: Catalyzes the conversion of 3-deoxy-D-arabino-heptulosonate 7-phosphate (DAHP) to dehydroquinate (DHQ). {ECO:0000255|HAMAP-Rule:MF_00110, ECO:0000269|PubMed:2514789}. EcoCyc product frame: AROB-MONOMER. Genomic coordinates: 3517398-3518486. EcoCyc protein note: Dehydroquinate synthase (DHQ synthase) is involved in the second step of the chorismate pathway, which leads to the biosynthesis of aromatic amino acids. DHQ synthase catalyzes the cyclization of 3-deoxy-D-arabino-heptulosonic acid 7-phosphate (DAHP) to dehydroquinate (DHQ) . In the course of this conversion the synthase apparently catalyzes an oxidation, a β-elimination, an intramolecular aldol condensation, and a reduction . DHQ synthase is a metalloenzyme that uses either Co2+ or Zn2+ as its metal cofactor. Although the Co2+ form of the enzyme has been reported have a higher specific activity, the bioavailability of Zn2+ in nature is much greater than Co2+. The presence of NAD+ as a cofactor is essential for catalytic activity. DHQ synthase appears to be synthesized constitutively and is not repressed by chorismate, any of the aromatic amino acids or by the regulator genes trpR and tyrR . The sequence for aroB has been determined and the protein overexpressed .

## Biological Role

Repressed by glaR (protein.P37338). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P07639|protein.P07639]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=aroB; function=+
- `represses` <-- [[protein.P37338|protein.P37338]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=aroB; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0011067,ECOCYC:EG10074,GeneID:947927`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3517398-3518486:-; feature_type=gene
