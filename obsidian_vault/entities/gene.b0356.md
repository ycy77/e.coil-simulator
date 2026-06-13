---
entity_id: "gene.b0356"
entity_type: "gene"
name: "frmA"
source_database: "NCBI RefSeq"
source_id: "gene-b0356"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0356"
  - "frmA"
---

# frmA

`gene.b0356`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0356`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

frmA (gene.b0356) is a gene entity. It encodes frmA (protein.P25437). Encoded protein function: FUNCTION: Has high formaldehyde dehydrogenase activity in the presence of glutathione and catalyzes the oxidation of normal alcohols in a reaction that is not GSH-dependent (PubMed:1731906). In addition, hemithiolacetals other than those formed from GSH, including omega-thiol fatty acids, also are substrates (PubMed:1731906). Also acts as a S-nitroso-glutathione reductase by catalyzing the NADH-dependent reduction of S-nitrosoglutathione (PubMed:11260719). {ECO:0000269|PubMed:11260719, ECO:0000269|PubMed:1731906}. EcoCyc product frame: ADHC-MONOMER. EcoCyc synonyms: adhC. Genomic coordinates: 378462-379571. EcoCyc protein note: Glutathione-dependent formaldehyde dehydrogenase (GS-FDH) belongs to the family of class III alcohol dehydrogenases. Glutathione and formaldehyde combine non-enzymatically to form hydroxymethylglutathione, the true substrate of the GS-FDH catalyzed reaction. The product, S-formylglutathione, is further metabolized to formic acid. The functional role of GS-FDH may be in the metabolism of endogenously formed formaldehyde and detoxifying exogenous formaldehyde . Transcription of the frmRAB operon is induced by formaldehyde, but not S-nitrosoglutathione .

## Biological Role

Repressed by frmR (protein.P0AAP3).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00071` Fatty acid degradation (KEGG)
- `eco00350` Tyrosine metabolism (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00625` Chloroalkane and chloroalkene degradation (KEGG)
- `eco00626` Naphthalene degradation (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01220` Degradation of aromatic compounds (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P25437|protein.P25437]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0AAP3|protein.P0AAP3]] `RegulonDB` `S` - regulator=FrmR; target=frmA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0001221,ECOCYC:EG50010,GeneID:944988`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:378462-379571:-; feature_type=gene
