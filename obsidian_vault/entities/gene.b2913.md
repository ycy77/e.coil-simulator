---
entity_id: "gene.b2913"
entity_type: "gene"
name: "serA"
source_database: "NCBI RefSeq"
source_id: "gene-b2913"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2913"
  - "serA"
---

# serA

`gene.b2913`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2913`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

serA (gene.b2913) is a gene entity. It encodes serA (protein.P0A9T0). Encoded protein function: FUNCTION: Catalyzes the reversible oxidation of 3-phospho-D-glycerate to 3-phosphonooxypyruvate, the first step of the phosphorylated L-serine biosynthesis pathway. Also catalyzes the reversible oxidation of 2-hydroxyglutarate to 2-oxoglutarate. {ECO:0000269|PubMed:8550422}. EcoCyc product frame: PGLYCDEHYDROG-MONOMER. Genomic coordinates: 3057178-3058410. EcoCyc protein note: D-3-phosphoglycerate dehydrogenase (SerA, PHGDH) catalyzes the first committed step in the biosynthesis of L-serine. The enzyme is regulated by allosteric end-product inhibition that shows cooperativity. Inhibition by serine acts primarily through reduction of catalytic velocity and has only a small effect on the Kms of the substrates; SerA is thus classified as a type V allosteric enzyme. SerA also has an α-ketoglutarate reductase activity, producing 2-hydroxyglutarate. Kinetically, the best SerA substrates are 3-phosphohydroxypyruvate (3PHP) and α-ketoglutarate (αKG), i.e. in vitro, the reaction equilibrium is skewed towards production of 3-phosphoglycerate (3PG) rather than the 3PHP intermediate required for serine biosynthesis . The hypothesis that the activities and reaction equilibria of SerA may play a role in recycling NADH back to NAD+ is supported by experimental data...

## Biological Role

Repressed by lrp (protein.P0ACJ0), nac (protein.Q47005). Activated by rpoD (protein.P00579), lrp (protein.P0ACJ0).

## Enriched Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A9T0|protein.P0A9T0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=serA; function=+
- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB|EcoCyc` `S` - regulator=Lrp; target=serA; function=-+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB` `S` - regulator=Lrp; target=serA; function=-+
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=serA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0009561,ECOCYC:EG10944,GeneID:945258`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3057178-3058410:-; feature_type=gene
