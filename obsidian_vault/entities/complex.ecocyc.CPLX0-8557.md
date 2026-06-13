---
entity_id: "complex.ecocyc.CPLX0-8557"
entity_type: "complex"
name: "ATP-dependent RNA helicase DeaD"
source_database: "EcoCyc"
source_id: "CPLX0-8557"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# ATP-dependent RNA helicase DeaD

`complex.ecocyc.CPLX0-8557`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8557`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P0A9P6|protein.P0A9P6]]

## Enriched Summary

The DeaD protein is a DEAD-box RNA helicase that participates in the assembly of the large, but not the small subunit of the ribosome and is involved in RNA degradation under low temperature growth conditions . DeaD appears to destabilize mRNA secondary structures in the translation initiation region of mRNAs . Subsequent experiments showed that DeaD may destabilize inhibitory stem-loop structures in the 5' UTR of EG10510, thereby enabling annealing of the small regulatory RNA DSRA-RNA DsrA , and that DeaD activates EG11140 mRNA translation by counteracting an inhibitory secondary structure formed between the uvrY mRNA leader and coding region . Reports differed on whether or not the RNA helicase activity of purified DeaD requires ATP hydrolysis. The measured ATP-independent unwinding activity may have been due to spontaneous base pair opening . The DEAD motif is required for efficient in vitro ATPase and helicase acivities and for in vivo function at 15°C . ATP-independent activities of DeaD include stimulation of RNA strand annealing, strand displacement, and RNA chaperone activity . Kinetic analysis of the annealing and strand displacement activities of DeaD support the hypothesis that the unwinding activity of DeaD is largely determined by the thermodynamic stability of its substrates...

## Biological Role

Catalyzes RXN-24178 (reaction.ecocyc.RXN-24178).

## Annotation

The DeaD protein is a DEAD-box RNA helicase that participates in the assembly of the large, but not the small subunit of the ribosome and is involved in RNA degradation under low temperature growth conditions . DeaD appears to destabilize mRNA secondary structures in the translation initiation region of mRNAs . Subsequent experiments showed that DeaD may destabilize inhibitory stem-loop structures in the 5' UTR of EG10510, thereby enabling annealing of the small regulatory RNA DSRA-RNA DsrA , and that DeaD activates EG11140 mRNA translation by counteracting an inhibitory secondary structure formed between the uvrY mRNA leader and coding region . Reports differed on whether or not the RNA helicase activity of purified DeaD requires ATP hydrolysis. The measured ATP-independent unwinding activity may have been due to spontaneous base pair opening . The DEAD motif is required for efficient in vitro ATPase and helicase acivities and for in vivo function at 15°C . ATP-independent activities of DeaD include stimulation of RNA strand annealing, strand displacement, and RNA chaperone activity . Kinetic analysis of the annealing and strand displacement activities of DeaD support the hypothesis that the unwinding activity of DeaD is largely determined by the thermodynamic stability of its substrates . The DeaD protein was found to be associated with a pre-50S ribosomal particle and interacts with EG10690-MONOMER , G7656-MONOMER and EG10859-MONOMER , as well as a number of ribosomal and other proteins . The presence of DeaD may assist in the efficient assembly of circularly permuted rRNAs, allowing them to function in the ribosome . DeaD is able to replace the function of the EG10844-MONOMER in the CPLX0-2381 . DeaD can stabilize overexpressed mRNAs , including EG10166 mRNA , or ma

## Outgoing Edges (4)

- `activates` --> [[gene.b0817|gene.b0817]] `EcoCyc` `database` - EcoCyc regulation TYPES=Protein-Mediated-Translation-Regulation
- `activates` --> [[gene.b1914|gene.b1914]] `EcoCyc` `database` - EcoCyc regulation TYPES=Protein-Mediated-Translation-Regulation
- `activates` --> [[gene.b1916|gene.b1916]] `EcoCyc` `database` - EcoCyc regulation TYPES=Protein-Mediated-Translation-Regulation
- `catalyzes` --> [[reaction.ecocyc.RXN-24178|reaction.ecocyc.RXN-24178]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0A9P6|protein.P0A9P6]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-8557`
- `QSPROTEOME:QS00198679`

## Notes

2*protein.P0A9P6
