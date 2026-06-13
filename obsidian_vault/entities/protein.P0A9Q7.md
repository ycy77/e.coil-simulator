---
entity_id: "protein.P0A9Q7"
entity_type: "protein"
name: "adhE"
source_database: "UniProt"
source_id: "P0A9Q7"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "adhE ana b1241 JW1228"
---

# adhE

`protein.P0A9Q7`

## Static

- Type: `protein`
- Source: `UniProt:P0A9Q7`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Under fermentative conditions, catalyzes the sequential NADH-dependent reduction of acetyl-CoA to acetaldehyde and then to ethanol (PubMed:10612730, PubMed:10922373, PubMed:17280641, PubMed:2015910, PubMed:6752127). Under aerobic conditions, despite the reversibility of the two NADH-coupled reactions, wild-type E.coli cannot grow on ethanol as the sole carbon and energy source due to the down-regulation of adhE transcription and the inactivation of the enzyme by metal-catalyzed oxidation (MCO) (PubMed:10922373). Nevertheless, in the presence of oxygen, AdhE may act as a hydrogen peroxide scavenger and have a protective role against oxidative stress (PubMed:12783863). {ECO:0000269|PubMed:10612730, ECO:0000269|PubMed:10922373, ECO:0000269|PubMed:12783863, ECO:0000269|PubMed:17280641, ECO:0000269|PubMed:2015910, ECO:0000269|PubMed:6752127}. Under anaerobic conditions, the multifunctional enzyme AdhE catalyzes the sequential reduction of acetyl-CoA to acetaldehyde and then to ethanol (see the FERMENTATION-PWY pathway). The two catalytic functions are conferred by its N-terminal aldehyde dehydrogenase (ALDH) domain and C-terminal iron-dependent alcohol dehydrogenase (ADH) domain...

## Biological Role

Catalyzes acetaldehyde:NAD+ oxidoreductase (CoA-acetylating) (reaction.R00228), primary_alcohol:NAD+ oxidoreductase (reaction.R00623), secondary_alcohol:NAD+ oxidoreductase (reaction.R00624), ethanol:NAD+ oxidoreductase (reaction.R00754), retinol:NAD+ oxidoreductase (reaction.R02124), 1-octanol:NAD+ oxidoreductase (reaction.R02878), trans-3-chloro-2-propene-1-ol:NAD+ oxidoreductase (reaction.R05233), cis-3-chloro-2-propene-1-ol:NAD+ oxidoreductase (reaction.R05234), and 2 more. Component of fused acetaldehyde-CoA dehydrogenase and Fe-dependent alcohol dehydrogenase (complex.ecocyc.ADHE-CPLX).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00071` Fatty acid degradation (KEGG)
- `eco00350` Tyrosine metabolism (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00625` Chloroalkane and chloroalkene degradation (KEGG)
- `eco00626` Naphthalene degradation (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01220` Degradation of aromatic compounds (KEGG)

## Annotation

FUNCTION: Under fermentative conditions, catalyzes the sequential NADH-dependent reduction of acetyl-CoA to acetaldehyde and then to ethanol (PubMed:10612730, PubMed:10922373, PubMed:17280641, PubMed:2015910, PubMed:6752127). Under aerobic conditions, despite the reversibility of the two NADH-coupled reactions, wild-type E.coli cannot grow on ethanol as the sole carbon and energy source due to the down-regulation of adhE transcription and the inactivation of the enzyme by metal-catalyzed oxidation (MCO) (PubMed:10922373). Nevertheless, in the presence of oxygen, AdhE may act as a hydrogen peroxide scavenger and have a protective role against oxidative stress (PubMed:12783863). {ECO:0000269|PubMed:10612730, ECO:0000269|PubMed:10922373, ECO:0000269|PubMed:12783863, ECO:0000269|PubMed:17280641, ECO:0000269|PubMed:2015910, ECO:0000269|PubMed:6752127}.

## Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00071` Fatty acid degradation (KEGG)
- `eco00350` Tyrosine metabolism (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00625` Chloroalkane and chloroalkene degradation (KEGG)
- `eco00626` Naphthalene degradation (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01220` Degradation of aromatic compounds (KEGG)

## Outgoing Edges (11)

- `catalyzes` --> [[reaction.R00228|reaction.R00228]] `KEGG` `database` - via EC:1.2.1.10
- `catalyzes` --> [[reaction.R00623|reaction.R00623]] `KEGG` `database` - via EC:1.1.1.1
- `catalyzes` --> [[reaction.R00624|reaction.R00624]] `KEGG` `database` - via EC:1.1.1.1
- `catalyzes` --> [[reaction.R00754|reaction.R00754]] `KEGG` `database` - via EC:1.1.1.1
- `catalyzes` --> [[reaction.R02124|reaction.R02124]] `KEGG` `database` - via EC:1.1.1.1
- `catalyzes` --> [[reaction.R02878|reaction.R02878]] `KEGG` `database` - via EC:1.1.1.1
- `catalyzes` --> [[reaction.R05233|reaction.R05233]] `KEGG` `database` - via EC:1.1.1.1
- `catalyzes` --> [[reaction.R05234|reaction.R05234]] `KEGG` `database` - via EC:1.1.1.1
- `catalyzes` --> [[reaction.R06917|reaction.R06917]] `KEGG` `database` - via EC:1.1.1.1
- `catalyzes` --> [[reaction.R06927|reaction.R06927]] `KEGG` `database` - via EC:1.1.1.1
- `is_component_of` --> [[complex.ecocyc.ADHE-CPLX|complex.ecocyc.ADHE-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=40 | EcoCyc protcplxs.col coefficient=40

## Incoming Edges (1)

- `encodes` <-- [[gene.b1241|gene.b1241]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A9Q7`
- `KEGG:ecj:JW1228;eco:b1241;ecoc:C3026_07295;`
- `GeneID:93775306;945837;`
- `GO:GO:0004022; GO:0005829; GO:0006115; GO:0006979; GO:0008198; GO:0008774; GO:0015976; GO:0016020; GO:0019664; GO:0042802; GO:0051260; GO:0120542`
- `EC:1.1.1.1; 1.2.1.10`

## Notes

Bifunctional aldehyde-alcohol dehydrogenase AdhE (Alcohol dehydrogenase E) [Includes: Acetaldehyde dehydrogenase [acetylating] (ACDH) (EC 1.2.1.10); Alcohol dehydrogenase (ADH) (EC 1.1.1.1)]
