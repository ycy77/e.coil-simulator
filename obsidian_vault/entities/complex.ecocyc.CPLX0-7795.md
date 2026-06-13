---
entity_id: "complex.ecocyc.CPLX0-7795"
entity_type: "complex"
name: "DNA-binding transcriptional dual regulator KdpE-phosphorylated"
source_database: "EcoCyc"
source_id: "CPLX0-7795"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: "CCO-CYTOSOL"
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "KdpE-P<sup>asp52</sup>"
  - "KdpE response regulator - phosphorylated"
---

# DNA-binding transcriptional dual regulator KdpE-phosphorylated

`complex.ecocyc.CPLX0-7795`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7795`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Location: CCO-CYTOSOL
- Complex type: `regulatory`
- Components: [[protein.P21866|protein.P21866]]

## Enriched Summary

KdpE is a transcriptional regulator involved in the regulation of genes involved in a high-affinity potassium (K+) uptake system . The genes of this system and their regulators are widely distributed among the gram-negative and gram-positive bacteria and archaea . KdpE activates expression of the kdpFABC operon encoding the P-type ATPase KdpFABC, a high-affinity potassium transport system. KdpE belongs to the two-component system KdpD/KdpE . The operon containing both genes, kdpE, encoding the response regulator, and kdpD, encoding the sensor kinase, is located next to and in the same direction as an operon (kdpFABC) regulated by KdpE . It has been suggested that sometimes the genes of the two operons are transcribed in only one transcript . In some species the arrangement of these genes in the genome is different than in Escherichia coli . KdpD exhibits both kinase and phosphatase activities towards KdpE . Under K+-limiting conditions or under osmotic stress imposed by a salt, autophosphorylation of KdpD at His-673 is stimulated . Subsequently, the phosphate group is transferred from KdpD to Asp-52 of KdpE , leading to the dimerization and activation of KdpE . Two domains of KdpE, the receiver and the DNA-binding domains, interact with KdpD for efficient signal transduction . At high concentrations of K+, the kinase activity of KdpD is inhibited...

## Annotation

KdpE is a transcriptional regulator involved in the regulation of genes involved in a high-affinity potassium (K+) uptake system . The genes of this system and their regulators are widely distributed among the gram-negative and gram-positive bacteria and archaea . KdpE activates expression of the kdpFABC operon encoding the P-type ATPase KdpFABC, a high-affinity potassium transport system. KdpE belongs to the two-component system KdpD/KdpE . The operon containing both genes, kdpE, encoding the response regulator, and kdpD, encoding the sensor kinase, is located next to and in the same direction as an operon (kdpFABC) regulated by KdpE . It has been suggested that sometimes the genes of the two operons are transcribed in only one transcript . In some species the arrangement of these genes in the genome is different than in Escherichia coli . KdpD exhibits both kinase and phosphatase activities towards KdpE . Under K+-limiting conditions or under osmotic stress imposed by a salt, autophosphorylation of KdpD at His-673 is stimulated . Subsequently, the phosphate group is transferred from KdpD to Asp-52 of KdpE , leading to the dimerization and activation of KdpE . Two domains of KdpE, the receiver and the DNA-binding domains, interact with KdpD for efficient signal transduction . At high concentrations of K+, the kinase activity of KdpD is inhibited . Under salt stress, the universal stress protein UspC binds to KdpD and stabilizes the KdpD-KdpE-DNA complex; therefore, this system can be activated even though K+ accumulates under this environmental condition . In addition, expression of the kdpFABC operon is regulated by the phosphoryl group transfer chain Ntr-PTS: dephosphorylated enzyme IIANtr binds to KdpD, and this interaction strongly stimulates KdpD kinase activity .

## Outgoing Edges (3)

- `represses` --> [[gene.b0953|gene.b0953]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b3714|gene.b3714]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b3995|gene.b3995]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P21866|protein.P21866]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-7795`
- `QSPROTEOME:QS00183029`

## Notes

2*protein.P21866
