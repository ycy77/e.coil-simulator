---
entity_id: "complex.ecocyc.CPLX0-8098"
entity_type: "complex"
name: "UDP-glucose 6-dehydrogenase"
source_database: "EcoCyc"
source_id: "CPLX0-8098"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# UDP-glucose 6-dehydrogenase

`complex.ecocyc.CPLX0-8098`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8098`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P76373|protein.P76373]]

## Enriched Summary

UDP-glucose dehydrogenase (Ugd) catalyzes the synthesis of UDP-glucuronic acid. Ugd activity is activated by tyrosine phosphorylation catalyzed by the tyrosine kinase Wzc . Ugd is also phosphorylated by Etk. Both Wzc and and Etk are BY-kinases which catalyze protein tyrosine phosphorylation. Phosphorylation of Ugd by Wzc was found to regulate the amount of colanic acid, while Etk is involved in the resistance to polymyxin B . ugd transcript levels are increased under growth conditions with low Mg2+ concentrations . Overproduction of UDP-glucose dehydrogenase reduces production of K5 polysaccharide during exogenous expression of the K5 biosynthesis gene cluster . ugd is found in a cluster of genes for the production of colanic acid . Mutagenesis of ugd showed the essential role of this gene in K30 biosynthesis and that there are no additional functional ugd copies. . Mutations in the UDP-glucuronic acid allosteric binding site decreased the binding affinity of the nucleotide triphosphate . In Salmonella, two 2-component system systems are required for ugd expression in response to low Mg2+ . UDP-glucose dehydrogenase (Ugd) catalyzes the synthesis of UDP-glucuronic acid. Ugd activity is activated by tyrosine phosphorylation catalyzed by the tyrosine kinase Wzc . Ugd is also phosphorylated by Etk. Both Wzc and and Etk are BY-kinases which catalyze protein tyrosine phosphorylation...

## Biological Role

Catalyzes UGD-RXN (reaction.ecocyc.UGD-RXN).

## Annotation

UDP-glucose dehydrogenase (Ugd) catalyzes the synthesis of UDP-glucuronic acid. Ugd activity is activated by tyrosine phosphorylation catalyzed by the tyrosine kinase Wzc . Ugd is also phosphorylated by Etk. Both Wzc and and Etk are BY-kinases which catalyze protein tyrosine phosphorylation. Phosphorylation of Ugd by Wzc was found to regulate the amount of colanic acid, while Etk is involved in the resistance to polymyxin B . ugd transcript levels are increased under growth conditions with low Mg2+ concentrations . Overproduction of UDP-glucose dehydrogenase reduces production of K5 polysaccharide during exogenous expression of the K5 biosynthesis gene cluster . ugd is found in a cluster of genes for the production of colanic acid . Mutagenesis of ugd showed the essential role of this gene in K30 biosynthesis and that there are no additional functional ugd copies. . Mutations in the UDP-glucuronic acid allosteric binding site decreased the binding affinity of the nucleotide triphosphate . In Salmonella, two 2-component system systems are required for ugd expression in response to low Mg2+ .

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.UGD-RXN|reaction.ecocyc.UGD-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P76373|protein.P76373]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-8098`
- `QSPROTEOME:QS00188519`

## Notes

2*protein.P76373
