---
entity_id: "protein.P25437"
entity_type: "protein"
name: "frmA"
source_database: "UniProt"
source_id: "P25437"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:1731906}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "frmA adhC b0356 JW0347"
---

# frmA

`protein.P25437`

## Static

- Type: `protein`
- Source: `UniProt:P25437`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:1731906}.

## Enriched Summary

FUNCTION: Has high formaldehyde dehydrogenase activity in the presence of glutathione and catalyzes the oxidation of normal alcohols in a reaction that is not GSH-dependent (PubMed:1731906). In addition, hemithiolacetals other than those formed from GSH, including omega-thiol fatty acids, also are substrates (PubMed:1731906). Also acts as a S-nitroso-glutathione reductase by catalyzing the NADH-dependent reduction of S-nitrosoglutathione (PubMed:11260719). {ECO:0000269|PubMed:11260719, ECO:0000269|PubMed:1731906}. Glutathione-dependent formaldehyde dehydrogenase (GS-FDH) belongs to the family of class III alcohol dehydrogenases. Glutathione and formaldehyde combine non-enzymatically to form hydroxymethylglutathione, the true substrate of the GS-FDH catalyzed reaction. The product, S-formylglutathione, is further metabolized to formic acid. The functional role of GS-FDH may be in the metabolism of endogenously formed formaldehyde and detoxifying exogenous formaldehyde . Transcription of the frmRAB operon is induced by formaldehyde, but not S-nitrosoglutathione .

## Biological Role

Catalyzes primary_alcohol:NAD+ oxidoreductase (reaction.R00623), secondary_alcohol:NAD+ oxidoreductase (reaction.R00624), ethanol:NAD+ oxidoreductase (reaction.R00754), retinol:NAD+ oxidoreductase (reaction.R02124), 1-octanol:NAD+ oxidoreductase (reaction.R02878), trans-3-chloro-2-propene-1-ol:NAD+ oxidoreductase (reaction.R05233), cis-3-chloro-2-propene-1-ol:NAD+ oxidoreductase (reaction.R05234), 1-hydroxymethylnaphthalene:NAD+ oxidoreductase (reaction.R06917), and 2 more. Component of S-(hydroxymethyl)glutathione dehydrogenase (complex.ecocyc.ADHC-CPLX).

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

FUNCTION: Has high formaldehyde dehydrogenase activity in the presence of glutathione and catalyzes the oxidation of normal alcohols in a reaction that is not GSH-dependent (PubMed:1731906). In addition, hemithiolacetals other than those formed from GSH, including omega-thiol fatty acids, also are substrates (PubMed:1731906). Also acts as a S-nitroso-glutathione reductase by catalyzing the NADH-dependent reduction of S-nitrosoglutathione (PubMed:11260719). {ECO:0000269|PubMed:11260719, ECO:0000269|PubMed:1731906}.

## Pathways

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

## Outgoing Edges (11)

- `catalyzes` --> [[reaction.R00623|reaction.R00623]] `KEGG` `database` - via EC:1.1.1.1
- `catalyzes` --> [[reaction.R00624|reaction.R00624]] `KEGG` `database` - via EC:1.1.1.1
- `catalyzes` --> [[reaction.R00754|reaction.R00754]] `KEGG` `database` - via EC:1.1.1.1
- `catalyzes` --> [[reaction.R02124|reaction.R02124]] `KEGG` `database` - via EC:1.1.1.1
- `catalyzes` --> [[reaction.R02878|reaction.R02878]] `KEGG` `database` - via EC:1.1.1.1
- `catalyzes` --> [[reaction.R05233|reaction.R05233]] `KEGG` `database` - via EC:1.1.1.1
- `catalyzes` --> [[reaction.R05234|reaction.R05234]] `KEGG` `database` - via EC:1.1.1.1
- `catalyzes` --> [[reaction.R06917|reaction.R06917]] `KEGG` `database` - via EC:1.1.1.1
- `catalyzes` --> [[reaction.R06927|reaction.R06927]] `KEGG` `database` - via EC:1.1.1.1
- `catalyzes` --> [[reaction.R06983|reaction.R06983]] `KEGG` `database` - via EC:1.1.1.284
- `is_component_of` --> [[complex.ecocyc.ADHC-CPLX|complex.ecocyc.ADHC-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0356|gene.b0356]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P25437`
- `KEGG:ecj:JW0347;eco:b0356;`
- `GeneID:944988;`
- `GO:GO:0004022; GO:0005737; GO:0005829; GO:0008270; GO:0042802; GO:0046294; GO:0051903; GO:0080007; GO:0106321; GO:0106322`
- `EC:1.1.1.-; 1.1.1.1; 1.1.1.284`

## Notes

S-(hydroxymethyl)glutathione dehydrogenase (EC 1.1.1.284) (Alcohol dehydrogenase class-3) (EC 1.1.1.1) (Alcohol dehydrogenase class-III) (Glutathione-dependent formaldehyde dehydrogenase) (FALDH) (FDH) (GSH-FDH) (EC 1.1.1.-)
